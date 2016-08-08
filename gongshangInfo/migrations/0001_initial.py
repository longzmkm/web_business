# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-08 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=35, verbose_name='公司名称')),
                ('person_name', models.CharField(max_length=35, verbose_name='人员名称')),
                ('position_name', models.CharField(default=None, max_length=35, verbose_name='职位')),
                ('regNO', models.FloatField(default=None, max_length=20, verbose_name='公司编号')),
            ],
            options={
                'verbose_name': '公司信息',
                'verbose_name_plural': '公司信息',
            },
        ),
    ]
