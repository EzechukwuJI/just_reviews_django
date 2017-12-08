# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 01:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20171121_0124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='datejoined',
        ),
        migrations.AlterField(
            model_name='comment',
            name='added',
            field=models.IntegerField(blank=True, default=1511228148.9971628),
        ),
        migrations.AlterField(
            model_name='product',
            name='added',
            field=models.FloatField(blank=True, default=1511228148.9971628, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='User',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]