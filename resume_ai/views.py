from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from .forms import ResumeUploadForm
from .models import Resume

import PyPDF2


class ResumeUploadView(LoginRequiredMixin, TemplateView):

    template_name = "resume_upload.html"

    def get(self, request, *args, **kwargs):

        form = ResumeUploadForm()

        return render(

            request,

            self.template_name,

            {
                'form': form
            }

        )

    def post(self, request, *args, **kwargs):

        form = ResumeUploadForm(

            request.POST,

            request.FILES

        )

        if form.is_valid():

            resume = form.save(commit=False)

            resume.user = request.user

            pdf_file = request.FILES['resume_file']

            pdf_reader = PyPDF2.PdfReader(pdf_file)

            extracted_text = ""

            for page in pdf_reader.pages:

                extracted_text += page.extract_text()

            resume.extracted_text = extracted_text


            # Skill Detection

            skills = [

                "Python",
                "Django",
                "FastAPI",
                "Flask",
                "JavaScript",
                "React",
                "HTML",
                "CSS",
                "MySQL",
                "PostgreSQL",
                "REST API",
                "Git",
                "GitHub"

            ]

            detected_skills = []

            resume_text_lower = extracted_text.lower()

            for skill in skills:

                if skill.lower() in resume_text_lower:

                    detected_skills.append(skill)


            resume.save()

            request.session['resume_skills'] = detected_skills
            request.session['resume_text'] = extracted_text

            return render(

                request,

                self.template_name,

                {

                    'form': ResumeUploadForm(),

                    'success': True,

                    'text': extracted_text[:2000],

                    'skills': detected_skills

                }

            )

        return render(

            request,

            self.template_name,

            {

                'form': form

            }

        )
import requests


import requests


class ResumeInterviewView(LoginRequiredMixin, TemplateView):

    template_name = "resume_interview.html"

    def get(self, request, *args, **kwargs):

        resume_text = request.session.get(
            'resume_text',
            ''
        )

        response = requests.post(

            "http://127.0.0.1:8001/resume-interview",

            json={

                "resume_text": resume_text

            }

        )

        data = response.json()

        return render(

            request,

            self.template_name,

            {

                'resume_text': resume_text,

                'questions': data.get('questions')

            }

        )
    
    def post(self, request, *args, **kwargs):

        questions = request.POST.getlist("questions")

        answers = request.POST.getlist("answers")

        response = requests.post(

            "http://127.0.0.1:8001/evaluate-interview",

            json={

                "questions": questions,

                "answers": answers

            }

        )

        data = response.json()

        return render(

            request,

            self.template_name,

            {

                "submitted": True,

                "questions": questions,

                "results": data.get("results"),

                "score": data.get("score"),

                "performance": data.get("performance")

            }

        )