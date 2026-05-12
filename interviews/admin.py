

# Register your models here.
from django.contrib import admin
from .models import InterviewCategory, InterviewSession

admin.site.register(InterviewCategory)
admin.site.register(InterviewSession)