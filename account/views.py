from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as log_user_in
from django.contrib.auth import logout as log_user_out
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from account.forms import LoginForm


@login_required
def index(request):
    return HttpResponseRedirect(reverse('account:profile'))


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            User.objects.create_user(username=username, password=password)
            return HttpResponseRedirect(reverse('ishare:index'))
    else:
        form = UserCreationForm()

    return render(request, 'account/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print('user:', user)
            log_user_in(request, user)
            # Redirect to a success page.
            next_url = request.POST.get('next')
            if next_url:
                return HttpResponseRedirect(next_url)
            else:
                return HttpResponseRedirect(reverse('ishare:index'))
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})


def logout(request):
    log_user_out(request)
    return HttpResponseRedirect(reverse('ishare:index'))


def profile(request):
    return HttpResponse('Profile')