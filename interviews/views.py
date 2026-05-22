from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

from .models import InterviewCategory, InterviewSession

import requests

class InterviewListView(LoginRequiredMixin, TemplateView):

    template_name = "interviews.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['categories'] = InterviewCategory.objects.all()

        return context


class StartInterviewView(LoginRequiredMixin, TemplateView):

    template_name = "start_interview.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        category_id = self.kwargs['pk']

        category = get_object_or_404(
            InterviewCategory,
            id=category_id
        )

        response = requests.get(
            f"http://127.0.0.1:8001/generate-question/{category.name}"
        )

        data = response.json()

        context['category'] = category

        context['questions'] = data.get('questions')

        return context


    def post(self, request, *args, **kwargs):

        questions = request.POST.getlist('questions')

        answers = []

        for key, value in request.POST.items():

            if key.startswith("answer"):

                answers.append(value)

        response = requests.post(

            "http://127.0.0.1:8001/evaluate-interview",

            json={

                "questions": questions,

                "answers": answers

            }

        )

        data = response.json()

        category_id = self.kwargs['pk']

        category = get_object_or_404(
            InterviewCategory,
            id=category_id
        )

        InterviewSession.objects.create(

            user=request.user,

            category=category,

            score=data.get('score'),

            performance=data.get('performance'),

            feedback=str(data.get('results'))

        )

        return render(

            request,

            'start_interview.html',

            {

                'submitted': True,

                'results': data.get('results'),

                'score': data.get('score'),

                'performance': data.get('performance')

            }

        )