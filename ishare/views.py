from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

from ishare.forms import UploadImageForm, CreateAlbumForm
from ishare.models import Entity, Image

def index(request):
    recent_images = Image.objects.order_by('entity__create_date')[:20]
    context = {
        'recent_images': recent_images,
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
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ishare:index'))
    else:
        form = CreateAlbumForm()
    return render(request, 'ishare/albums.html', {'form': form})


def photo_direct(request, photo_id):
    image = get_object_or_404(Image, pk=photo_id)
    return HttpResponse(image.photo, content_type='image/jpeg')


def photo_detail(request, photo_id):
    image = get_object_or_404(Image, pk=photo_id)
    context = {
        'image': image,
    }
    return render(request, 'ishare/photo_detail.html', context)