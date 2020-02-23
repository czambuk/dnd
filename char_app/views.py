# from django.db import models
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.views import View


class ViewCharacterSheet(View):
    def get(self, request):
        return TemplateResponse(
            request,
            "char_app/view_char_chart.html",
        )


class NewCharacterSheet(View):
    def get(self, request):
        return TemplateResponse(
            request,
            "char_app/new_char_chart.html"
        )

    # def post(self,request):
    #     return