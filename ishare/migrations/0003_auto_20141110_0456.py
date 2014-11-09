# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ishare', '0002_auto_20141110_0452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='id',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='id',
        ),
        migrations.RemoveField(
            model_name='image',
            name='id',
        ),
        migrations.AlterField(
            model_name='album',
            name='entity',
            field=models.OneToOneField(primary_key=True, to='ishare.Entity', serialize=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='entity',
            field=models.OneToOneField(primary_key=True, to='ishare.Entity', serialize=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='entity',
            field=models.OneToOneField(primary_key=True, to='ishare.Entity', serialize=False),
            preserve_default=True,
        ),
    ]
