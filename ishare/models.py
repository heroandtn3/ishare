from django.core.urlresolvers import reverse
from django.templatetags.static import static
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
        return '%s - %s' % (self.entity.id, self.title)

    def image_number(self):
        return self.image_set.count()

    def thumbnail_url(self):
        if self.image_set.count() > 0:
            first_image = self.image_set.all()[0]
            return reverse('ishare:photo_direct', args=(first_image.pk,))
        else:
            return static('ishare/images/default.png')

class Image(models.Model):
    title = models.CharField(max_length=255)
    last_modified_date = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos')

    entity = models.OneToOneField(Entity, limit_choices_to={
            'entity_type': Entity.IMAGE
        }, primary_key=True)
    album = models.ForeignKey(Album)

    def __str__(self):
        return '%s - %s' % (self.entity.id, self.title)

    def comment_number(self):
        return self.entity.comments.count()

    def voteup_number(self):
        return self.entity.vote_set.filter(is_vote_up=True).count()

    def votedown_number(self):
        return self.entity.vote_set.filter(is_vote_up=False).count()

    def recent_comments(self):
        return self.entity.comments.all()


class Comment(models.Model):
    content = models.TextField()
    last_modified_date = models.DateTimeField(auto_now=True)

    entity = models.OneToOneField(Entity, limit_choices_to={
            'entity_type': Entity.COMMENT
        }, primary_key=True, related_name='+')
    target_entity = models.ForeignKey(Entity, related_name='comments')

    def __str__(self):
        return '%s' % self.pk


class Vote(models.Model):
    is_vote_up = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)

    creator = models.OneToOneField(User)
    target_entity = models.ForeignKey(Entity)

    def __str__(self):
        return '%s' % self.pk