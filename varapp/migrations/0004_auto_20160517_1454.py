# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-17 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('varapp', '0003_auto_20160317_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variantsdb',
            name='size',
            field=models.BigIntegerField(null=True),
        ),
    ]