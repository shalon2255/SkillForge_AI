from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import InterviewCategory


class InterviewListView(LoginRequiredMixin, TemplateView):

    template_name = "interviews.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['categories'] = InterviewCategory.objects.all()

        return context