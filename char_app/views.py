# from django.db import models
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.views import View


class CharacterSheet(View):
    def get(self, request):
        return TemplateResponse(
            request,
            "char_app/char_chart.html",
        )

    def post(self, request):
        return TemplateResponse(
            request,
            "char_app/char_chart.html",
        )
