# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('updata_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('ad_name', models.CharField(max_length=20)),
                ('ad_image', models.ImageField(upload_to='ad')),
                ('ad_link', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('updata_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('cag_name', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Goodsinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('updata_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('goods_name', models.CharField(max_length=20)),
                ('goods_price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('goods_image', models.ImageField(upload_to='')),
                ('goods_short', models.CharField(max_length=100)),
                ('goods_look', models.IntegerField(default=0)),
                ('goods_sales', models.IntegerField(default=0)),
                ('goods_status', models.BooleanField(default=True)),
                ('goods_unit', models.CharField(max_length=10)),
                ('goods_cag', models.ForeignKey(to='goods.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
