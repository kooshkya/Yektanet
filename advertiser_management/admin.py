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
    actions = ['approve_ads', 'disapprove_ads']

    @admin.action(description="Approve Ads")
    def approve_ads(self, request, queryset):
        queryset.update(approved=True)

    @admin.action(description="Disapprove Ads")
    def disapprove_ads(self, request, queryset):
        queryset.update(approved=False)


@admin.register(Click)
class ClickAdmin(admin.ModelAdmin):
    pass


@admin.register(ViewEvent)
class ViewEventAdmin(admin.ModelAdmin):
    pass
