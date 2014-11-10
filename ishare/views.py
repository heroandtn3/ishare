from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from ishare.forms import UploadImageForm
from ishare.models import Entity

def index(request):
    return render(request, 'ishare/index.html')


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