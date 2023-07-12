from django.db.models import Count, Q, F
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, RedirectView, CreateView, ListView
from django.utils import timezone

from .forms import CreateAdForm, CreateAdvertiserForm
from .models import *


# Create your views here.

class IndexView(TemplateView):
    template_name = "advertiser_management/index.html"

    def get_context_data(self, **kwargs):
        raw_context = super().get_context_data(**kwargs)
        raw_context['ads'] = Ad.objects.all().order_by('advertiser__name')
        raw_context['advertisers'] = Advertiser.objects.all()
        return raw_context


class CreateAdView(CreateView):
    model = Ad
    form_class = CreateAdForm
    template_name = "advertiser_management/create_ad.html"
    success_url = reverse_lazy("advertiser_management:ad_page", args=())


class CreateAdvertiserView(CreateView):
    model = Advertiser
    form_class = CreateAdvertiserForm
    template_name = "advertiser_management/create_advertiser.html"
    success_url = reverse_lazy("advertiser_management:index")


class AdPageView(TemplateView):
    template_name = "advertiser_management/ads.html"

    def get_context_data(self, **kwargs):
        raw_context = super().get_context_data(**kwargs)
        raw_context['advertisers'] = Advertiser.objects.all()
        return raw_context


class HandleClickView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['pk'])
        return ad.link


class AdStatsView(ListView):
    model = Ad
    template_name = "advertiser_management/ad_stats.html"
    context_object_name = "ads"

    def get_context_data(self, *, object_list=None, **kwargs):
        con = super().get_context_data(**kwargs)
        hour = self.kwargs['hour']
        con['hour'] = hour
        max_time = timezone.now() - timezone.timedelta(hours=hour)
        min_time = max_time - timezone.timedelta(hours=1)
        con['total_views'] = ViewEvent.objects.filter(view_time__lt=max_time, view_time__gt=min_time).count()
        con['total_clicks'] = Click.objects.filter(click_time__lt=max_time, click_time__gt=min_time).count()
        con['ctr'] = con['total_clicks'] / con['total_views'] if con['total_views'] > 0 else None
        con['min_time'] = min_time
        con['max_time'] = max_time
        clicks = list(Click.objects.all())
        dt_sum = timezone.timedelta()
        for click in clicks:
            view = ViewEvent.objects.filter(view_ip=click.clicker_ip, ad=click.ad, view_time__lt=click.click_time)[0]
            print(f"click: {click}, view: {view}")
            click.delta_time = click.click_time - view.view_time
            dt_sum += click.delta_time
        dt_sum /= len(clicks)
        con['avg_dt'] = dt_sum
        object_list = list(Ad.objects.all())
        for o in object_list:
            o.click_count = 0
            o.view_count = 0
        self.get_clicks(object_list, min_time, max_time)
        self.get_views(object_list, min_time, max_time)
        con['ads'] = object_list
        con['object_list'] = object_list
        return con

    @staticmethod
    def get_clicks(object_list: list, min_time, max_time):
        clicks = Click.objects.filter(click_time__lt=max_time, click_time__gt=min_time)
        for click in clicks:
            ad = click.ad
            object_in_list = object_list[object_list.index(ad)]
            object_in_list.click_count = object_in_list.click_count + 1 if object_in_list.click_count is not None else 1

    @staticmethod
    def get_views(object_list: list, min_time, max_time):
        views = ViewEvent.objects.filter(view_time__lt=max_time, view_time__gt=min_time)
        for view in views:
            ad = view.ad
            object_in_list = object_list[object_list.index(ad)]
            object_in_list.view_count = object_in_list.view_count + 1 if object_in_list.view_count is not None else 1

    def get_queryset(self):
        return None
        # hour = self.kwargs['hour']
        # max_time = timezone.now() - timezone.timedelta(hours=hour)
        # min_time = max_time - timezone.timedelta(hours=1)
        # return Ad.objects.annotate(
        #     click_count=Count('click_set',
        #                       filter=(Q(click_set__click_time__lt=max_time) & Q(click_set__click_time__gt=min_time)),
        #                       distinct=True)
        #     ,
        #     view_count=Count('view_set',
        #                      filter=(Q(click_set__click_time__lt=max_time) & Q(view_set__view_time__gt=min_time)),
        #                      distinct=True)
        # )
