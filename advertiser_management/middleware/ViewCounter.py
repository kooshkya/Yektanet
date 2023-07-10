from ..models import *
from django.utils import timezone


class ViewCounter:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"going for {request.path}")
        if request.path.endswith("ad_page/"):
            for advertiser in Advertiser.objects.all():
                for ad in advertiser.ad_set.all():
                    ViewEvent.objects.create(ad=ad, view_time=timezone.now(), view_ip=request.META["REMOTE_ADDR"])
        return self.get_response(request)
