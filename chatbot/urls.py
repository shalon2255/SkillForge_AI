from django.urls import path

from .views import (
    ChatbotView,
    NewChatView,
    ChatSessionView,
    DeleteChatView
)


urlpatterns = [

    path(
        '',
        ChatbotView.as_view(),
        name='chatbot'
    ),

    path(
        'new-chat/',
        NewChatView.as_view(),
        name='new-chat'
    ),

    path(
        'session/<int:pk>/',
        ChatSessionView.as_view(),
        name='chat-session'
    ),
path(
    'delete/<int:pk>/',
    DeleteChatView.as_view(),
    name='delete-chat'
),
]