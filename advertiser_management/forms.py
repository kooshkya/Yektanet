from django.forms import ModelForm
from .models import Ad, Advertiser


class CreateAdForm(ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'imgUrl', 'link', 'advertiser', 'approved']


class CreateAdvertiserForm(ModelForm):
    class Meta:
        model = Advertiser
        exclude = []
