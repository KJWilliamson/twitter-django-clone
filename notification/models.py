from django.db import models
from django.utils import timezone
from tweet.models import Tweet
from twitteruser.models import TwitterUser


# Create your models here.
class Notification(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, )
    profile = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    notification_total = models.IntegerField(default=0)
    tweet_seen = models.BooleanField(default=False)
