from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Message
from users.models import User


@login_required
def chat_view(request, user_id, messages=None):
    recipient = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        message = request.POST.get('message', '')
        if message:
            new_message = Message.objects.create(sender=request.user, recipient=recipient, message=message)
            new_message.save()
            return redirect('chat:chat', user_id=user_id)
        else:
            messages.error(request, 'Введите текст сообщения')
            return redirect('chat:chat', user_id=user_id)
    else:
        messages = Message.objects.filter(Q(sender=request.user, recipient=recipient) | Q(sender=recipient, recipient=request.user)).order_by('timestamp')
        messages = Paginator(messages, 20)
        page_number = request.GET.get('page')
        messages_page = messages.get_page(page_number)
        return render(request, 'chat/chat.html', {'messages': messages_page, 'recipient': recipient})
