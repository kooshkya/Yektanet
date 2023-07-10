from django.contrib import admin
from advertiser_management.models import *


# Register your models here.
@admin.register(Advertiser)
class AdvertiserAdmin(admin.ModelAdmin):
    pass


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    pass
