from django.contrib import admin
from advertiser_management.models import *


# Register your models here.
@admin.register(Advertiser)
class AdvertiserAdmin(admin.ModelAdmin):
    pass


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ['title', 'advertiser', 'approved']
    list_editable = ['approved',]
    search_fields = ['title']
    list_filter = ['approved']
    actions = ['approve_ads', 'disapprove_ads']

    @admin.action(description="Approve Ads")
    def approve_ads(self, request, queryset):
        queryset.update(approved=True)

    @admin.action(description="Disapprove Ads")
    def disapprove_ads(self, request, queryset):
        queryset.update(approved=False)


@admin.register(Click)
class ClickAdmin(admin.ModelAdmin):
    list_display = ['id', 'ad', 'click_time', 'clicker_ip']


@admin.register(ViewEvent)
class ViewEventAdmin(admin.ModelAdmin):
    list_display = ['id', 'ad', 'view_time', 'view_ip']
