from django.template.response import TemplateResponse
from django.shortcuts import redirect
from django.views import View
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import (CreateView,
                                  DeleteView,
                                  FormView,
                                  ListView,
                                  UpdateView
                                  )


class HomePage(View):
    def get(self, request):
        return TemplateResponse(
            request,
            "landing_page/main_site.html"
        )


class LoginPageView(LoginView):
    redirect_authenticated_user = True


class LogoutPageView(LogoutView):
    redirect_authenticated_user = True


class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = 'landing_page/form.html'
    success_url = '/login'

    def form_valid(self, form):
        del form.cleaned_data['password_repeat']
        user = User.objects.create_user(**form.cleaned_data)
        return redirect('/login')
