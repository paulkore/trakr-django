# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trakr', '0006_auto_20150317_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='weight',
            field=models.DecimalField(decimal_places=3, null=True, default=None, max_digits=10),
            preserve_default=True,
        ),
    ]
