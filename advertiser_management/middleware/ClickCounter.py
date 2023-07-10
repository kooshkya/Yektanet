import re
from django.shortcuts import get_object_or_404
from django.utils import timezone
from ..models import Ad, Click


class ClickCounter:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        pattern = re.compile(r"/click/(?P<id>[0-9]+)/")
        matcher = pattern.match(path)
        if matcher:
            print(f"Processing click {request.path}")
            ad_id = matcher.group("id")
            ad = get_object_or_404(Ad, pk=ad_id)
            Click.objects.create(ad=ad, clicker_ip=request.META["REMOTE_ADDR"], click_time=timezone.now())

        return self.get_response(request)
