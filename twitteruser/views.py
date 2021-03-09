# render is what puts variables & info on the templates
# https://docs.djangoproject.com/en/3.1/ref/models/querysets/#campus-indianapolis
# https://learndjango.com/tutorials/django-slug-tutorial
# https://docs.djangoproject.com/en/3.1/ref/class-based-views/base/

from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from tweet.models import Tweet


# Create your views here.
@login_required
def index(request):
    # all_users = TwitterUser.objects.all()
    # users_following = current_users.following.all()
    all_tweets = Tweet.objects.all().order_by('created_at').reverse()
    main_user = TwitterUser.objects.get(username=request.user)
    main_user_tweets = Tweet.objects.filter(tweeter=main_user).order_by('-created_at').reverse()
    tweet_count = Tweet.objects.filter(tweeter__username=request.user).count()
    following_count = len(main_user.following.all())
    home_tweets = Tweet.objects.filter(tweeter__in=request.user.following.all()).order_by('-created_at')
    users_list = TwitterUser.objects.all()
    return render(request, 'index.html', {'all_tweets': all_tweets, 'tweet_count': tweet_count,
                                          'following_count': following_count, 'users_list': users_list,
                                          'home_tweets': home_tweets, 'main_user_tweets': main_user_tweets})


def profile_view(request):
    all_tweets = Tweet.objects.all().order_by('created_at').reverse()
    # users_following = profile_user.following.all()
    profile_user = TwitterUser.objects.get(username=request.user)
    tweet_counter = Tweet.objects.filter(tweeter__username=request.user).count()
    follow_count = len(profile_user.following.all())
    profile_tweets = Tweet.objects.filter(tweeter=profile_user).order_by('created_at').reverse()
    following_list = TwitterUser.objects.all()
    return render(request, 'profile.html', {'all_tweets': all_tweets, 'profile_user': profile_user,
                                            'tweet_counter': tweet_counter, 'profile_tweets': profile_tweets,
                                            'following_list': following_list, 'follow_count': follow_count})


# def user_detail_view(request, username):
#     current_user = TwitterUser.objects.filter(username=username).first()
#     user_tweets = Tweet.objects.filter(tweeter=current_user).order_by('created_at').reverse()
#     users_following = current_user.following.all()
#     if current_user.is_authenticated:
#         following = request.user.following.all()
#     else:
#         following = []
#
#     return render(request, 'user_detail.html', {'current_user': current_user, 'user_tweets': user_tweets,
#                                                 'following': following, 'users_following': users_following})
def user_detail_view(request, username):
    current_user = TwitterUser.objects.get(username=username)
    user_tweets = Tweet.objects.filter(tweeter=current_user).order_by('created_at').reverse()
    users_following = current_user.following.all()
    if current_user.is_authenticated:
        following = request.user.following.all()
    else:
        following = []
    return render(request, 'user_detail.html', {'current_user': current_user, 'user_tweets': user_tweets,
                                                'following': following, 'users_following': users_following})


def follow_view(request, user_id):
    current_users = TwitterUser.objects.get(id=user_id)
    follow = TwitterUser.objects.get(id=request.user.id)
    follow.following.add(current_users)
    # following.following += 1
    # my_peeps = current_users.following.all()
    follow.save()
    # current_users.user_followers.add(following_user)
    # current_users.followers += 1
    current_users.save()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


def unfollow_view(request, user_id):
    current_users = TwitterUser.objects.get(id=user_id)
    following = TwitterUser.objects.get(id=request.user.id)
    # following_user.followed_users.remove(current_users)
    following.following -= 1
    following.save()
    # current_users.user_followers.remove(following_user)
    # current_users.followers -= 1
    current_users.save()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
