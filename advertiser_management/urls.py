from django.urls import path
from . import views

app_name = "advertiser_management"

urlpatterns = [
    path("", views.index, name="index"),
    path("ad_page/", views.ad_page, name="ad_page"),
    path("create_ad/", views.create_ad, name="create_ad"),
    path("click/<int:ad_id>/", views.handle_click, name="handle_click")
]
