# https://learndjango.com/tutorials/django-slug-tutorial
from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from notification.models import Notification
from twitteruser.models import TwitterUser


# Create your views here.
@login_required
def notification_view(request):
    username = request.user
    twitteruser = TwitterUser.objects.get(username=username)
    notifications = Notification.objects.filter(profile=twitteruser)
    new_notifications = [
        notification for notification in notifications
        if notification.not_viewed][::-1]
    for new_notification in new_notifications:
        new_notification.not_viewed = False
        new_notification.save()
    return render(request, 'notifications.html', {'new_notifications': new_notifications, 'twitteruser': twitteruser})
