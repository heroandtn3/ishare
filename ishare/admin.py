from django.contrib import admin

from ishare.models import Entity, Image, Album, Comment, Vote

admin.site.register(Entity)
admin.site.register(Image)
admin.site.register(Album)
admin.site.register(Comment)
admin.site.register(Vote)
