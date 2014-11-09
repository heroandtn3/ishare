# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ishare', '0003_auto_20141110_0456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='target_entity',
            field=models.ForeignKey(to='ishare.Entity', related_name='+'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vote',
            name='target_entity',
            field=models.ForeignKey(to='ishare.Entity', related_name='+'),
            preserve_default=True,
        ),
    ]
