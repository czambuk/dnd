# from django.db import models
from django.template.response import TemplateResponse
from django.http import HttpResponse, HttpRequest
from django.views import View
from .models import Player, Character, Campaign


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

    def post(self, request):
        name = request.POST.get("charname")
        classlevel = request.POST.get("classlevel")
        background = request.POST.get("background")
        playername = request.POST.get("playername")
        race = request.POST.get("race")
        alignment = request.POST.get("alignment")
        experiencepoints = request.POST.get("experiencepoints")

        player = Player.objects.get(name=playername)

        Character.objects.create(
            name=name,
            basic_class=classlevel,
            race=race,
            player_id=player.id,
        )

        return TemplateResponse(
            request,
            "char_app/new_char_chart.html",
        )


class HomePage(View):
    def get(self, request):
        return TemplateResponse(
            request,
            "char_app/base.html",
        )
