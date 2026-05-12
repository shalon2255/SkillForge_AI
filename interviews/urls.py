from django.urls import path
from .views import InterviewListView

urlpatterns = [

    path('', InterviewListView.as_view(), name='interviews'),

]