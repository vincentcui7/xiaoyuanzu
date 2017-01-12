# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-29 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workapp', '0011_auto_20161229_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houseinfo',
            name='housetype',
            field=models.CharField(blank=True, choices=[('一室一厅一卫', '一室一厅一卫'), ('三室一厅两卫', '三室一厅两卫'), ('三室一厅一卫', '三室一厅一卫'), ('二室一厅一卫', '二室一厅一卫'), ('三室两厅两卫', '三室两厅两卫'), ('四室两厅两卫', '四室两厅两卫')], max_length=200),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11),
        ),
    ]
