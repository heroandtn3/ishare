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

    def __str__(self):
        return '%s: %s' % (self. entity_type, self.id)


class Album(models.Model):
    title = models.CharField(max_length=255)
    private = models.BooleanField(default=False)
    last_modified_date = models.DateTimeField(auto_now=True)

    entity = models.OneToOneField(Entity, limit_choices_to={
            'entity_type': Entity.ALBUM
        }, primary_key=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    title = models.CharField(max_length=255)
    last_modified_date = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos')

    entity = models.OneToOneField(Entity, limit_choices_to={
            'entity_type': Entity.IMAGE
        }, primary_key=True)
    album = models.ForeignKey(Album)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    last_modified_date = models.DateTimeField(auto_now=True)

    entity = models.OneToOneField(Entity, limit_choices_to={
            'entity_type': Entity.COMMENT
        }, primary_key=True)
    target_entity = models.ForeignKey(Entity, related_name='+')

    def __str__(self):
        return self.id


class Vote(models.Model):
    is_vote_up = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)

    creator = models.OneToOneField(User)
    target_entity = models.ForeignKey(Entity, related_name='+')

    def __str__(self):
        return self.id