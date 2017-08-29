# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 19:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('droneExchange', '0006_auto_20170828_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_me', models.TextField()),
                ('pricing', models.DecimalField(decimal_places=2, max_digits=6)),
                ('video_type', models.CharField(choices=[('video', 'video'), ('photography', 'photography'), ('video and photography', 'video and photography')], max_length=100)),
                ('cities', models.ManyToManyField(to='droneExchange.City')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
