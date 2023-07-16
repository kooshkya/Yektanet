from django.db import models
import django.utils.timezone
from django.utils import timezone

# Create your models here.
class Advertiser(models.Model):
    name = models.TextField()

    def ads(self):
        return self.ad_set.all()

    def views(self):
        count = 0
        for ad in self.ad_set.all():
            count += ad.views()
        return count

    def clicks(self):
        count = 0
        for ad in self.ad_set.all():
            count += ad.clicks()
        return count

    def __str__(self):
        return f"{self.id}- {self.name}"


class Ad(models.Model):
    title = models.TextField()
    imgUrl = models.TextField()
    link = models.TextField()
    advertiser = models.ForeignKey(to="Advertiser", on_delete=models.CASCADE, related_name="ad_set")
    approved = models.BooleanField(blank=False, null=False, default=False)

    def views(self):
        return self.view_set.count()

    def clicks(self):
        return self.click_set.count()

    def __str__(self):
        return f"{self.id}- {self.title}"


class Click(models.Model):
    click_time = models.DateTimeField(default=django.utils.timezone.now)
    clicker_ip = models.GenericIPAddressField()
    ad = models.ForeignKey(to="Ad", on_delete=models.CASCADE, related_name="click_set")


class ViewEvent(models.Model):
    view_time = models.DateTimeField(default=django.utils.timezone.now)
    view_ip = models.GenericIPAddressField()
    ad = models.ForeignKey(to="Ad", on_delete=models.CASCADE, related_name="view_set")


class HourlyReport(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    clicks = models.IntegerField()
    views = models.IntegerField()
    time = models.DateTimeField(default=timezone.now)
