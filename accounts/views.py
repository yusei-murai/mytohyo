from .models import CustomUser
from timeline.models import Question
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .forms import ProfileForm

"""
class ProfileDetail(LoginRequiredMixin, generic.DetailView, generic.ListView):
    model = CustomUser
    template_name = 'account/detail.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['questions'] = Question.objects.all
        return context

detail = ProfileDetail.as_view()
"""
