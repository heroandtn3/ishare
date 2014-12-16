from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.templatetags.static import static

from ishare.forms import UploadImageForm, CreateAlbumForm
from ishare.models import Entity, Image
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