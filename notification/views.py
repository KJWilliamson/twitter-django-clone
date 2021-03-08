# https://learndjango.com/tutorials/django-slug-tutorial
# https://docs.djangoproject.com/en/3.1/topics/class-based-views/
from django.shortcuts import render, HttpResponseRedirect
from notification.models import Notification

# Create your views here.


def notification_view(request):
    notification = Notification.objects.filter(profile=request.user)
    for view in notification:
        view.delete()

    # return HttpResponseRedirect('notification')

    return render(request, 'notifications.html', {'notification': notification})
