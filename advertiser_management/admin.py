from django.contrib import admin
from advertiser_management.models import *


# Register your models here.
@admin.register(Advertiser)
class AdvertiserAdmin(admin.ModelAdmin):
    pass


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ['title', 'advertiser', 'approved']
    search_fields = ['title']
    list_filter = ['approved']


@admin.register(Click)
class ClickAdmin(admin.ModelAdmin):
    pass


@admin.register(ViewEvent)
class ViewEventAdmin(admin.ModelAdmin):
    pass
