from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

import requests


class ChatbotView(LoginRequiredMixin, TemplateView):

    template_name = "chatbot.html"

    def get(self, request, *args, **kwargs):

        if 'chat_history' not in request.session:

            request.session['chat_history'] = []

        return render(

            request,

            self.template_name,

            {
                'chat_history': request.session['chat_history']
            }

        )

    def post(self, request, *args, **kwargs):

        user_message = request.POST.get('message')

        response = requests.post(

            "http://127.0.0.1:8001/chatbot",

            json={
                "message": user_message
            }

        )

        data = response.json()

        bot_response = data.get('response')

        chat_history = request.session.get(
            'chat_history',
            []
        )

        chat_history.append({

            'user': user_message,

            'bot': bot_response

        })

        request.session['chat_history'] = chat_history

        return render(

            request,

            self.template_name,

            {
                'chat_history': chat_history
            }

        )