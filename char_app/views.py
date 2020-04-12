# from django.db import models
from django.template.response import TemplateResponse
from django.http import HttpResponse, HttpRequest
from django.views import View
from .models import Player, Character


class ViewCharacterSheet(View):
    def get(self, request, id):
        if Character.objects.get(id=id) is not None:
            character = Character.objects.get(id=id)
            title = character.name
        else:
            title = "Error"
        dict = {"page_title": title}
        return TemplateResponse(
            request,
            "char_app/char_view.html",
            context=dict,
        )


class NewCharacterSheet(View):
    def get(self, request):
        title = f"New PC"
        dict = {"page_title": title}
        return TemplateResponse(
            request,
            "char_app/char_new.html",
            context=dict,
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
            "char_app/char_new.html",
        )
