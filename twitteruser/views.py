from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from django.utils import timezone
from notification.models import Notification


# Create your views here.
@login_required
def index(request):
    tweets = TwitterUser.objects.all().order_by('-date_joined')
    return render(request, 'index.html', {'tweets': tweets})


def user_detail_view(request, username):
    current_user = TwitterUser.objects.filter(username=username).first()
    tweets = Tweet.objects.filter(tweeter=current_user).order_by('-date_joined')
    if current_user.is_authenticated:
        followers = request.user.followers.all()
    else:
        followers = []

    return render(request, 'user_detail.html', {'current_user': current_user, 'tweets': tweets, 'followers': followers})


def follow_view(request, username):
    current_user = request.user
    following_user = TwitterUser.objects.filter(username=username).first()
    current_user.followers.add(following_user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def unfollow_view(request, username):
    current_user = request.user
    following_user = TwitterUser.objects.filter(username=username).first()
    current_user.followers.delete(following_user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
