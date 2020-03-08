# from django.db import models
from django.template.response import TemplateResponse
# from django.http import HttpResponse, HttpRequest
from django.views import View


# from .models import Player, Character, Campaign

class HomePage(View):
    def get(self, request):
        return TemplateResponse(
            request,
            "landing_page/main_site.html",
        )
