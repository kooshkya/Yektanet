from django.urls import path
from . import views

app_name = "advertiser_management"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("ad_page/", views.AdPageView.as_view(), name="ad_page"),
    path("create_ad/", views.CreateAdView.as_view(), name="create_ad"),
    path("create_advertiser/", views.CreateAdvertiserView.as_view(), name="create_advertiser"),
    path("click/<int:pk>/", views.HandleClickView.as_view(), name="handle_click")
]
