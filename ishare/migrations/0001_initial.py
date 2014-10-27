# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('private', models.BooleanField(default=False)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('content', models.TextField()),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('entity_type', models.CharField(max_length=3, choices=[('com', 'Comment'), ('alb', 'Album'), ('img', 'Image')])),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
                ('photo', models.ImageField(upload_to='photos')),
                ('album', models.ForeignKey(to='ishare.Album')),
                ('entity', models.ForeignKey(to='ishare.Entity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('is_vote_up', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('target_entity', models.ForeignKey(related_name='+', to='ishare.Entity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comment',
            name='entity',
            field=models.ForeignKey(to='ishare.Entity'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='target_entity',
            field=models.ForeignKey(related_name='+', to='ishare.Entity'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='album',
            name='entity',
            field=models.ForeignKey(to='ishare.Entity'),
            preserve_default=True,
        ),
    ]
