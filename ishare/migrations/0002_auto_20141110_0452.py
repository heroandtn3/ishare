# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ishare', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='entity',
            field=models.OneToOneField(to='ishare.Entity'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='entity',
            field=models.OneToOneField(to='ishare.Entity'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='target_entity',
            field=models.OneToOneField(to='ishare.Entity', related_name='+'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='entity',
            field=models.OneToOneField(to='ishare.Entity'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vote',
            name='creator',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vote',
            name='target_entity',
            field=models.OneToOneField(to='ishare.Entity', related_name='+'),
            preserve_default=True,
        ),
    ]
