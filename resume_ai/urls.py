from django.urls import path

from .views import ResumeUploadView
from .views import ResumeUploadView, ResumeInterviewView

urlpatterns = [

    path(
        '',
        ResumeUploadView.as_view(),
        name='resume-upload'
    ),
path(
    'interview/',
    ResumeInterviewView.as_view(),
    name='resume-interview'
),
]