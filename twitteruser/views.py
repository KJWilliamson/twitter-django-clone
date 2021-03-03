from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from tweet.models import Tweet


# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')
