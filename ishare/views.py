from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.templatetags.static import static
from django.core import serializers

import json

from ishare.forms import UploadImageForm, CreateAlbumForm
from ishare.models import Entity, Image, Album, Comment
from ishare import dao

def index(request):
    recent_images = dao.get_recent_images()
    recent_albums = dao.get_recent_albums()
    context = {
        'recent_images': recent_images,
        'recent_albums': recent_albums
    }
    return render(request, 'ishare/index.html', context)


@login_required
def upload(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ishare:index'))
    else:
        form = UploadImageForm()
    return render(request, 'ishare/upload.html', {'form': form})


@login_required
def albums(request):
    context = {}
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ishare:index'))
    else:
        form = CreateAlbumForm()
        recent_albums = dao.get_user_albums(request.user)
        context['recent_albums'] = recent_albums
    context['form'] = form
    return render(request, 'ishare/albums.html', context)


def photo_direct(request, photo_id):
    image = get_object_or_404(Image, pk=photo_id)
    return HttpResponse(image.photo, content_type='image/jpeg')


def photo_detail(request, photo_id):
    image = get_object_or_404(Image, pk=photo_id)
    context = {
        'image': image,
    }
    return render(request, 'ishare/photo_detail.html', context)

def photo_json_recent_comment(request, photo_id):
    image = get_object_or_404(Image, pk=photo_id)
    recent_comments = image.recent_comments()

    data = [dao.comment_to_json(c) for c in recent_comments]
    return HttpResponse(json.dumps(data), content_type="application/json")

def photo_json_send_comment(request, photo_id):
    if request.method == 'GET':
        return HttpResponse('Not support method')

    if not request.user.is_authenticated():
        data = {
            'error': {
                'code': 1,
                'msg': 'You are not logon!'
            }
        }
    else:
        image = get_object_or_404(Image, pk=photo_id)
        message = request.POST.get('message')
        if not message:
            data = {
                'error': {
                    'code': 2,
                    'msg': 'Empty comment'
                }
            }
        else:
            entity = Entity(entity_type=Entity.COMMENT, creator=request.user)
            entity.save()
            comment = Comment(
                content=message,
                entity=entity,
                target_entity=image.entity)
            comment.save()
            data = dao.comment_to_json(comment)
    return HttpResponse(json.dumps(data), content_type="application/json")

def album_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    context = {
        'album': album
    }
    return render(request, 'ishare/album_detail.html', context)