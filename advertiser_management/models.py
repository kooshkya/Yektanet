from django.db import models
import django.utils.timezone


# Create your models here.
class Advertiser(models.Model):
    name = models.TextField()
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def ads(self):
        return self.ad_set.all()


class Ad(models.Model):
    title = models.TextField()
    imgUrl = models.TextField()
    link = models.TextField()
    advertiser = models.ForeignKey(to="Advertiser", on_delete=models.CASCADE, null=True, related_name="ad_set")


class Click(models.Model):
    click_time = models.DateTimeField(default=django.utils.timezone.now)
    clicker_ip = models.GenericIPAddressField()
    ad = models.ForeignKey(to="Ad", on_delete=models.CASCADE)


class ViewEvent(models.Model):
    view_time = models.DateTimeField(default=django.utils.timezone.now)
    view_ip = models.GenericIPAddressField()
    ad = models.ForeignKey(to="Ad", on_delete=models.CASCADE)
