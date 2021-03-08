# render is what puts variables & info on the templates
# https://docs.djangoproject.com/en/3.1/ref/models/querysets/#campus-indianapolis
# https://learndjango.com/tutorials/django-slug-tutorial
# https://docs.djangoproject.com/en/3.1/ref/class-based-views/base/

from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from tweet.models import Tweet


# Create your views here.
@login_required
def index(request):
    # all_users = TwitterUser.objects.all()
    all_tweets = Tweet.objects.all().order_by('created_at').reverse()
    main_user = TwitterUser.objects.get(username=request.user)
    tweet_count = Tweet.objects.filter(tweeter__username=request.user).count()
    following_count = len(main_user.following.all())
    home_tweets = Tweet.objects.filter(tweeter__in=request.user.following.all()).order_by('-created_at')
    # notification = Tweet.objects.filter(tweeter=request.user).filter(notification_seen=False)
    users_list = TwitterUser.objects.all()
    return render(request, 'index.html', {'all_tweets': all_tweets, 'tweet_count': tweet_count, 'following_count': following_count, 'users_list': users_list, 'home_tweets': home_tweets})


def profile_view(request):
    all_tweets = Tweet.objects.all().order_by('created_at').reverse()
    tweet_count = Tweet.objects.filter(tweeter=request.user).order_by('-created_at')
    return render(request, 'profile.html', {'all_tweets': all_tweets})


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
    current_user.followers.remove(following_user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
