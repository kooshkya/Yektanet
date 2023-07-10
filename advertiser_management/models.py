from django.db import models
import django.utils.timezone


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


class Ad(models.Model):
    title = models.TextField()
    imgUrl = models.TextField()
    link = models.TextField()
    advertiser = models.ForeignKey(to="Advertiser", on_delete=models.CASCADE, null=True, related_name="ad_set")

    def views(self):
        return self.viewevent_set.count()

    def clicks(self):
        return self.click_set.count()


class Click(models.Model):
    click_time = models.DateTimeField(default=django.utils.timezone.now)
    clicker_ip = models.GenericIPAddressField()
    ad = models.ForeignKey(to="Ad", on_delete=models.CASCADE)


class ViewEvent(models.Model):
    view_time = models.DateTimeField(default=django.utils.timezone.now)
    view_ip = models.GenericIPAddressField()
    ad = models.ForeignKey(to="Ad", on_delete=models.CASCADE)
