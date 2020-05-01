# from django.db import models
from django.template.response import TemplateResponse
# from django.http import HttpResponse, HttpRequest
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import (CreateView,
                                  DeleteView,
                                  FormView,
                                  ListView,
                                  UpdateView
                                  )


# from .models import Player, Character, Campaign

class HomePage(View):
    def get(self, request):
        return TemplateResponse(
            request,
            "landing_page/main_site.html",
        )


class LoginPageView(LoginView):
    redirect_authenticated_user = True


class LogoutPageView(LogoutView):
    redirect_authenticated_user = True

# TODO Rejestracja użytkownika
