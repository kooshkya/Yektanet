from celery import shared_task


@shared_task(name="advertiser_management.record_hourly_records")
def record_hourly_records():
    print("hello")
