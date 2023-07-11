from django.forms import ModelForm
from .models import Ad


class CreateAdForm(ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'imgUrl', 'link', 'advertiser', 'approved']
