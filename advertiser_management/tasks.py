from celery import shared_task
from .models import Ad, Click, ViewEvent, HourlyReport, DailyReport
from django.utils import timezone
from django.db.models import Count, Q, F, Sum


@shared_task(name='advertiser_management.record_daily_records')
def record_daily_records():
    max_time = timezone.now() - timezone.timedelta()
    min_time = max_time - timezone.timedelta(days=1)
    hourlies = HourlyReport.objects.filter(time__gt=min_time, time__lt=max_time)
    hourlies = hourlies.values('ad').annotate(click_count=Sum('clicks'), view_count=Sum('views'))
    for entry in hourlies:
        DailyReport.objects.create(ad=Ad.objects.get(pk=entry.get('ad')), clicks=entry.get('click_count'), views=entry.get('view_count'))


@shared_task(name="advertiser_management.record_hourly_records")
def record_hourly_records():
    print('hi hour!')
    max_time = timezone.now() - timezone.timedelta(hours=0)
    min_time = max_time - timezone.timedelta(hours=1)
    object_list = list(Ad.objects.all())
    clicks = Click.objects.filter(click_time__lt=max_time, click_time__gt=min_time)
    clicks = clicks.values('ad_id').annotate(click_count=Count('ad_id'))
    for click in clicks:
        ad = Ad.objects.get(pk=click['ad_id'])
        object_in_list = object_list[object_list.index(ad)]
        object_in_list.click_count = click['click_count']
    views = ViewEvent.objects.filter(view_time__lt=max_time, view_time__gt=min_time)
    views = views.values('ad_id').annotate(view_count=Count('ad_id'))
    for view in views:
        ad = Ad.objects.get(pk=view['ad_id'])
        object_in_list = object_list[object_list.index(ad)]
        object_in_list.view_count = view['view_count']

    for obj in object_list:
        if not hasattr(obj, 'click_count'):
            obj.click_count = 0
        if not hasattr(obj, 'view_count'):
            obj.view_count = 0
        HourlyReport.objects.create(ad=obj, clicks=obj.click_count, views=obj.view_count, time=timezone.now())
