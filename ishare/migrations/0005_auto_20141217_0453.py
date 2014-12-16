# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ishare', '0004_auto_20141110_0459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='target_entity',
            field=models.ForeignKey(related_name='comments', to='ishare.Entity'),
            preserve_default=True,
        ),
    ]
