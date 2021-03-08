"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from authentication.views import signup_view, login_view, logout_view
from notification.views import notification_view
from twitteruser.views import index
from tweet.views import create_tweet_view, tweet_detail
from twitteruser.views import user_detail_view, unfollow_view, follow_view, profile_view



urlpatterns = [
    path('', index, name='homepage'),
    path('signup/', signup_view, name='signup'),
    path('signup/accounts/login/', login_view, name='login'),
    path('login/', login_view, name='login'),
    path('accounts/login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('user/<str:username>/', user_detail_view, name='userdetail'),
    path('createtweet/', create_tweet_view, name='createtweet'),
    path('tweet/<int:tweet_id>/', tweet_detail, name='tweetdetail'),
    path('notifications/', notification_view, name='notifications'),
    path('unfollow/<str:username>/', unfollow_view, name='unfollow'),
    path('follow/<str:username>/', follow_view, name='follow'),
    path('profile/', profile_view, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
