# https://pypi.org/project/django-notifications-hq/
# https://hackersandslackers.com/creating-django-views/
# https://realpython.com/get-started-with-django-1/
# https://stackoverflow.com/questions/47244036/using-django-login-required-mixin
# https://docs.djangoproject.com/en/3.1/topics/auth/default/
# https://docs.djangoproject.com/en/3.0/topics/auth/default/#django.contrib.auth.mixins.AccessMixin.get_login_url
# https://learndjango.com/tutorials/django-best-practices-user-permissions

from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from notification.models import Notification
from tweet.models import Tweet
from tweet.forms import TweetForm
from django.contrib import messages
import re


# Create your views here.

def tweet_detail(request, tweet_id):
    tweet_id = Tweet.objects.get(id=tweet_id)
    notify = Notification.objects.filter(profile=request.user)
    return render(request, 'tweet_detail.html', {'tweet_id': tweet_id, 'notify': notify})


@login_required
def create_tweet_view(request):
    # if request.method == 'POST':
    form = TweetForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        new_tweet = Tweet.objects.create(
            text=data['text'],
            tweeter=request.user,

        )
        mentions = re.findall(r'@(\w+)', data.get('text'))
        if mentions:
            for mention in mentions:
                match = TwitterUser.objects.get(username=mention)
                if match:
                    Notification.objects.create(
                        profile=match, tweet=new_tweet
                    )

        return HttpResponseRedirect(reverse('homepage'))

    else:
        return render(request, 'generic_form.html', {'form': form})
