from django.urls import path
from .views import InterviewListView, StartInterviewView

urlpatterns = [

    path(
        '',
        InterviewListView.as_view(),
        name='interviews'
    ),

    path(
        'start/<int:pk>/',
        StartInterviewView.as_view(),
        name='start_interview'
    ),

]