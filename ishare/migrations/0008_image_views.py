# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ishare', '0007_auto_20141222_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='views',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
