from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from interviews.models import InterviewSession


class HomeView(TemplateView):

    template_name = "home.html"


class DashboardView(LoginRequiredMixin, TemplateView):

    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        interviews = InterviewSession.objects.filter(
            user=self.request.user
        ).order_by('-created_at')

        total_interviews = interviews.count()

        average_score = 0

        if total_interviews > 0:

            total_score = sum(
                interview.score
                for interview in interviews
            )

            average_score = round(
                total_score / total_interviews,
                1
            )

        context['total_interviews'] = total_interviews

        context['average_score'] = average_score

        context['recent_interviews'] = interviews[:5]

        return context