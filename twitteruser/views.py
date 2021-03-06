# render is what puts variables & info on the templates
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from django.utils import timezone
from notification.models import Notification


# Create your views here.
@login_required
def index(request):
    # all_users = TwitterUser.objects.all()
    all_tweets = Tweet.objects.all().order_by('created_at').reverse()
    return render(request, 'index.html', {'all_tweets': all_tweets})


def user_detail_view(request, username):
    current_user = TwitterUser.objects.filter(username=username).first()
    user_tweets = Tweet.objects.filter(tweeter=current_user).order_by('created_at')
    if current_user.is_authenticated:
        following = request.user.following.all()
    else:
        following = []

    return render(request, 'user_detail.html', {'current_user': current_user, 'user_tweets': user_tweets, 'following': following})


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
