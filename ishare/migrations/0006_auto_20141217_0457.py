# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ishare', '0005_auto_20141217_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='entity',
            field=models.OneToOneField(related_name='+', serialize=False, to='ishare.Entity', primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vote',
            name='target_entity',
            field=models.ForeignKey(to='ishare.Entity'),
            preserve_default=True,
        ),
    ]
