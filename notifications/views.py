from django.shortcuts import render, reverse, HttpResponseRedirect
from .forms import AddMessageForm
from .models import Notification, Message
from user_app.models import HeroUser
import re

# Create your views here.


def messages_home(request):
    messages = Message.objects.all().order_by('-time_date')
    return render(request, 'messages.html', {'messages': messages})


def add_message(request):
    if request.method == 'POST':
        form = AddMessageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_message = Message.objects.create(
                text=data['text'],
                assigned_message=request.user,
            )
            mentions = re.findall(r'(\B@\w+)', new_message.text)
            for mention in mentions:
                name = mention.lstrip('@')
                user_mentioned = HeroUser.objects.filter(
                    username=name
                    ).first()
                Notification.objects.create(
                    mention=new_message,
                    mentioned_user=user_mentioned
                )
            return HttpResponseRedirect(reverse('home'))

    form = AddMessageForm()
    return render(request, 'generic_form.html', {'form': form})


def message_details(request, message_id: int):
    message = Message.objects.get(id=message_id)
    return render(
        request,
        'message_details.html',
        {'message': message}
        )


def notification_view(request):
    notifications = 'Notifications go here'
    return render(
        request,
        'notifications.html',
        {
            'notifications': notifications
            }
        )
