from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.shortcuts import redirect, get_object_or_404
import requests

from .models import ChatSession, ChatMessage


class ChatbotView(LoginRequiredMixin, TemplateView):

    template_name = "chatbot.html"

    def get(self, request, *args, **kwargs):

        sessions = ChatSession.objects.filter(
            user=request.user
        ).order_by('-created_at')

        current_session = sessions.first()

        messages = []

        if current_session:

            messages = current_session.messages.all().order_by(
                'created_at'
            )

        return render(

            request,

            self.template_name,

            {

                'chat_sessions': sessions,

                'current_session': current_session,

                'messages': messages

            }

        )

    def post(self, request, *args, **kwargs):

        user_message = request.POST.get('message')

        if not user_message or not user_message.strip():

            return redirect('chatbot')

        sessions = ChatSession.objects.filter(
            user=request.user
        ).order_by('-created_at')

        current_session = sessions.first()

        if not current_session:

            current_session = ChatSession.objects.create(

                user=request.user,

                title=user_message[:40]

            )

        elif current_session.title == "New Chat":

            current_session.title = user_message[:40]

            current_session.save()

        response = requests.post(

            "http://127.0.0.1:8001/chatbot",

            json={
                "message": user_message
            }

        )

        data = response.json()

        bot_response = data.get(
            'response',
            'No response received.'
        )

        ChatMessage.objects.create(

            session=current_session,

            is_user=True,

            message=user_message

        )

        ChatMessage.objects.create(

            session=current_session,

            is_user=False,

            message=bot_response

        )

        return redirect('chatbot')


class NewChatView(LoginRequiredMixin, View):

    def post(self, request):

        ChatSession.objects.create(

            user=request.user,

            title="New Chat"

        )

        return redirect('chatbot')


class ChatSessionView(LoginRequiredMixin, TemplateView):

    template_name = "chatbot.html"

    def get(self, request, pk):

        sessions = ChatSession.objects.filter(
            user=request.user
        ).order_by('-created_at')

        current_session = get_object_or_404(

            ChatSession,

            id=pk,

            user=request.user

        )

        messages = current_session.messages.all().order_by(
            'created_at'
        )

        return render(

            request,

            self.template_name,

            {

                'chat_sessions': sessions,

                'current_session': current_session,

                'messages': messages

            }

        )
class DeleteChatView(LoginRequiredMixin, View):

    def post(self, request, pk):

        session = get_object_or_404(

            ChatSession,

            id=pk,

            user=request.user

        )

        session.delete()

        return redirect('chatbot')