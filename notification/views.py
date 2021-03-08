# https://learndjango.com/tutorials/django-slug-tutorial
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from notification.models import Notification
from twitteruser.models import TwitterUser
from tweet.models import Tweet


# Create your views here.
@login_required
# def notification_view(request):
#     notification = Notification.objects.filter(profile=request.user)
#     count = 0
#     new = []
#     for view in notification:
#         if view.notification_seen == False:
#             new.append(view.tweet)
#             view.notification_seen = True
#             count += 1
#             view.save()
#     return render(request, 'notifications.html', {'notification': notification, 'new': new, 'count': count})

@login_required
def notification_view(request):
    notification = Notification.objects.filter(profile=request.user)
    for view in notification:
        view.delete()
    return render(request, 'notifications.html', {'notification': notification})
