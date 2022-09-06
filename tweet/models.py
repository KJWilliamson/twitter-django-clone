# created_at from ghostpost & bugtracker
from django.db import models
from django.utils import timezone
from twitteruser.models import TwitterUser


# Create your models here.
class Tweet(models.Model):
    text = models.CharField(max_length=140)
    created_at = models.DateTimeField(default=timezone.now)
    # bring TwitterUser in like we did in bugtracker with CustomUser
    tweeter = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, related_name='tweeter')

    def __str__(self):
        return self.text
