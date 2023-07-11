from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView, CreateView

from .forms import CreateAdForm
from .models import *


# Create your views here.

class IndexView(TemplateView):
    template_name = "advertiser_management/index.html"

    def get_context_data(self, **kwargs):
        raw_context = super().get_context_data(**kwargs)
        raw_context['ads'] = Ad.objects.all().order_by('advertiser__name')
        raw_context['advertisers'] = Advertiser.objects.all()


class CreateAdView(CreateView):
    model = Ad
    form_class = CreateAdForm
    template_name = "advertiser_management/create_ad.html"
    success_url = reverse_lazy("advertiser_management:ad_page", args=())


def create_advertiser(request):
    if request.method == 'POST':
        name = request.POST["name"]
        advertiser = Advertiser(name=name)
        advertiser.save()
        return HttpResponseRedirect(reverse("advertiser_management:index"))
    elif request.method == 'GET':
        return render(request, "advertiser_management/create_advertiser.html", None)


def ad_page(request):
    return render(request, "advertiser_management/ads.html", context={
        'advertisers': Advertiser.objects.all(),
    })


def handle_click(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)
    return HttpResponseRedirect(ad.link)
