# Generated by Django 4.2.3 on 2023-07-16 11:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_management', '0007_alter_ad_advertiser_alter_click_ad_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HourlyReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clicks', models.IntegerField()),
                ('views', models.IntegerField()),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertiser_management.ad')),
            ],
        ),
    ]
