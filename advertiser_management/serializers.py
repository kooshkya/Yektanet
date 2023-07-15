from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *


class AdModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'title', 'imgUrl', 'link', 'advertiser', 'approved', 'views', 'clicks']
        read_only_fields = ['id']


class AdvertiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertiser
        fields = ['id', 'name']
        read_only_fields = ['id']


class AdSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    imgUrl = serializers.CharField()
    link = serializers.CharField()
    advertiser = serializers.PrimaryKeyRelatedField(queryset=Advertiser.objects.all())
    approved = serializers.BooleanField()
    views = serializers.IntegerField(read_only=True)
    clicks = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return Ad.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.imgUrl = validated_data.get('imgUrl', instance.imgUrl)
        instance.link = validated_data.get('link', instance.link)
        instance.advertiser = validated_data.get('advertiser', instance.advertiser)
        instance.approved = validated_data.get('approved', instance.approved)
        instance.save()
        return instance

