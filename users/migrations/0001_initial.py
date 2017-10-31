# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('updata_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('user_name', models.CharField(max_length=30)),
                ('user_pwd', models.CharField(max_length=70)),
                ('user_email', models.CharField(max_length=50)),
                ('user_tel', models.CharField(max_length=11)),
                ('user_addr', models.CharField(max_length=50)),
                ('user_code', models.CharField(max_length=9)),
                ('user_recv', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
