from django.urls import path, include
from . import views

app_name = "advertiser_management"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("ad_page/", views.AdPageView.as_view(), name="ad_page"),
    path("api/ad_page/", views.AdPageAPI.as_view(), name="ad_page_api"),
    path("create_ad/", views.CreateAdView.as_view(), name="create_ad"),
    path("api/create_ad/", views.CreateAdAPI.as_view(), name="create_ad_api"),
    path("create_advertiser/", views.CreateAdvertiserView.as_view(), name="create_advertiser"),
    path("api/create_advertiser/", views.CreateAdvertiserAPI.as_view(), name="create_advertiser_api"),
    path("click/<int:pk>/", views.HandleClickView.as_view(), name="handle_click"),
    path("ad_stats/<int:hour>/", views.AdStatsView.as_view(), name="ad_stats"),
    path("api/ad_stats/<int:hour>/", views.AdStatsAPI.as_view(), name="ad_stats_api"),
]
