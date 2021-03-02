# using all my previous assessments
# https://docs.djangoproject.com/en/3.1/topics/db/examples/
# https://stackoverflow.com/questions/58794639/how-to-make-follower-following-system-with-django-model
# https://www.youtube.com/watch?v=gf2-J9YOMcc
# https://stackoverflow.com/questions/60083124/how-to-check-in-django-model-manytomanyfield-is-symmetrical-if-symmetrical-false
# https://stackoverflow.com/questions/9410647/how-to-filter-model-results-for-multiple-values-for-a-many-to-many-field-in-djan

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class TwitterUser(AbstractUser):
    followers = models.ManyToManyField('self', symmetrical=False, related_name='twitter_followers')
    following = models.ManyToManyField('self', symmetrical=False, related_name='following_on_twitter')

    def __str__(self):
        return self.username
