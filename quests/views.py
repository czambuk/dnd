from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import redirect
# Forms
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


# class AllQuestsView(View):
#     def get(self, request):
#         return TemplateResponse(
#             request,
#             "quests.html"
#         )


class AllQuestsView(LoginRequiredMixin, ListView):
    template_name = 'quests.html'
    model = Quest
