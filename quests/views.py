from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import redirect
# Forms
from quests.forms import QuestForm
# Models
from quests.models import Quest
# User
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
# Views
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView,
                                  DeleteView,
                                  ListView,
                                  UpdateView,
                                  )


class AllQuestsView(LoginRequiredMixin, ListView):
    template_name = 'quests.html'
    model = Quest


class QuestCreateView(LoginRequiredMixin, CreateView):
    form_class = QuestForm
    template_name = 'landing_page/form.html'
    success_url = '/view_quests'


