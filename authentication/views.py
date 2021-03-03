# used my customuser as a reference
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from authentication.forms import SignupForm, LoginForm
from twitteruser.models import TwitterUser


# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = TwitterUser.objects.create_user(
                username=data['username'],
                password=data['password']
            )

            login(request, new_user)
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = SignupForm()
    return render(request, 'generic_form.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )

            login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = LoginForm()

    return render(request, 'generic_form.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
