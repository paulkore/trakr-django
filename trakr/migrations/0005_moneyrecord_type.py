# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trakr', '0004_auto_20150223_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='moneyrecord',
            name='type',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
