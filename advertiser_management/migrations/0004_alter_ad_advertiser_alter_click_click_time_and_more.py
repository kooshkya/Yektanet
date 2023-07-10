# Generated by Django 4.2.3 on 2023-07-10 13:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_management', '0003_remove_ad_clicks_remove_ad_views_alter_ad_advertiser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='advertiser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ads', to='advertiser_management.advertiser'),
        ),
        migrations.AlterField(
            model_name='click',
            name='click_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 10, 13, 3, 3, 803208, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='viewevent',
            name='view_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 10, 13, 3, 3, 803562, tzinfo=datetime.timezone.utc)),
        ),
    ]
