# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_auto_20160213_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='code',
            field=models.CharField(blank=True, max_length=254),
        ),
    ]
