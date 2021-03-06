# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 00:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField(max_length=200)),
                ('pub_date', models.DateField(auto_now=True)),
                ('added', models.IntegerField(blank=True, default=1511222460.4213774)),
                ('image', models.FileField(blank=True, null=True, upload_to='comment-imgs/')),
                ('backs', models.IntegerField(default=0)),
                ('backedBy', models.CharField(blank=True, default='test', max_length=10000, null=True)),
                ('comment_product_slug', models.CharField(blank=True, max_length=100, null=True)),
                ('posted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('views', models.IntegerField(default=0)),
                ('details', models.CharField(max_length=100)),
                ('categorysaver', models.CharField(blank=True, max_length=100, null=True)),
                ('thumbsUp', models.IntegerField(default=0)),
                ('thumbsDown', models.IntegerField(default=0)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('comments', models.IntegerField(default=0)),
                ('pub_date', models.DateField(auto_now=True)),
                ('added', models.FloatField(blank=True, default=1511222460.4188735, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='product-imgs/')),
                ('thumbsUpBy', models.CharField(blank=True, default='test', max_length=10000, null=True)),
                ('thumbsDownBy', models.CharField(blank=True, default='test', max_length=10000, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reviews.Category')),
                ('posted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='profile-imgs/')),
                ('datejoined', models.DateField(auto_now=True)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Product')),
            ],
            options={
                'verbose_name_plural': 'User Accounts',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Product'),
        ),
    ]
