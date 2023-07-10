from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import *


# Create your views here.
def index(request):
    return render(request, "advertiser_management/index.html", None)


def create_ad(request):
    if request.method == 'GET':
        return render(request, "advertiser_management/create_ad.html", None)
    elif request.method == 'POST':
        advertiser_id = int(request.POST["advertiser_id"])
        selected_advertiser = get_object_or_404(Advertiser, pk=advertiser_id)
        image_url = request.POST["image_url"]
        title = request.POST["title"]
        link = request.POST["link"]

        ad = Ad(advertiser=selected_advertiser, title=title, link=link, imgUrl=image_url)
        ad.save()
        return HttpResponseRedirect(reverse("advertiser_management:ad_page", args=()))


def ad_page(request):
    return render(request, "advertiser_management/ads.html", context={
        'advertisers': Advertiser.objects.all(),
    })


def handle_click(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)
    ad.clicks += 1
    ad.advertiser.clicks += 1
    return HttpResponseRedirect(ad.link)
