from django.db import models

from django.contrib.auth.models import User


class Entity(models.Model):
    COMMENT = 'com'
    ALBUM = 'alb'
    IMAGE = 'img'
    ENTITY_TYPE_CHOICES = (
        (COMMENT, 'Comment'),
        (ALBUM, 'Album'),
        (IMAGE, 'Image')
    )
    entity_type = models.CharField(max_length=3, choices=ENTITY_TYPE_CHOICES)
    create_date = models.DateTimeField(auto_now_add=True)

    creator = models.ForeignKey(User)


class Album(models.Model):
    title = models.CharField(max_length=255)
    private = models.BooleanField(default=False)
    last_modified_date = models.DateTimeField(auto_now=True)

    entity = models.ForeignKey(Entity, limit_choices_to={
            'entity_type': Entity.ALBUM
        })


class Image(models.Model):
    title = models.CharField(max_length=255)
    last_modified_date = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos')

    entity = models.ForeignKey(Entity, limit_choices_to={
            'entity_type': Entity.IMAGE
        })
    album = models.ForeignKey(Album)


class Comment(models.Model):
    content = models.TextField()
    last_modified_date = models.DateTimeField(auto_now=True)

    entity = models.ForeignKey(Entity, limit_choices_to={
            'entity_type': Entity.COMMENT
        })
    target_entity = models.ForeignKey(Entity, related_name='+')


class Vote(models.Model):
    is_vote_up = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)

    creator = models.ForeignKey(User)
    target_entity = models.ForeignKey(Entity, related_name='+')