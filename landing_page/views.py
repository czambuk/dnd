# Django
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import redirect
# Forms
from .forms import UserCreateForm, ContactForm, CustomAuthForm
# User
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
# Views
from django.views import View
from django.views.generic import CreateView


class HomePage(View):
    def get(self, request):
        return TemplateResponse(
            request,
            "landing_page/main_site.html"
        )


class LoginPageView(LoginView):
    redirect_authenticated_user = True
    authentication_form = CustomAuthForm


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


class ContactPage(View):
    def get(self, request):
        form = ContactForm
        return TemplateResponse(
            request,
            "landing_page/contact_page.html",
            context={"form": form},
        )

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']

            message = "{0} Wysłał wiadomość:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('Nowa wiadomość', message, sender_email, ['gramywdnd@gmail.com'])
            return HttpResponse('Dzięki za kontakt!')
