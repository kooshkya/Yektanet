from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
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
        return con

    def get_queryset(self):
        hour = self.kwargs['hour']
        max_time = timezone.now() - timezone.timedelta(hours=hour)
        min_time = max_time - timezone.timedelta(hours=1)
        return Ad.objects.annotate(
            click_count=Count('click_set',
                              filter=(Q(click_set__click_time__lt=max_time) & Q(click_set__click_time__gt=min_time)),
                              distinct=True)
            ,
            view_count=Count('view_set',
                             filter=(Q(click_set__click_time__lt=max_time) & Q(view_set__view_time__gt=min_time)),
                             distinct=True)
        )
