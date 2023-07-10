from django.db import models


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
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    advertiser = models.ForeignKey(to="Advertiser", on_delete=models.SET_NULL, null=True, related_name="ad_set")
