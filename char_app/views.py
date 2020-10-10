# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
# Views
from django.views import View
from django.views.generic import ListView, DetailView
# Models
from .models import Character, Classes, Races, Alignments


class ViewCharacterSheet(LoginRequiredMixin, View):
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


class NewCharacterSheet(LoginRequiredMixin, View):
    def get(self, request):
        title = f"Nowy bohater"
        classes = Classes.objects.all
        races = Races.objects.all
        alignments = Alignments.objects.all

        dict = {"page_title": title,
                "classes": classes,
                "races": races,
                "alignments": alignments,
                }

        return TemplateResponse(
            request,
            "char_app/char_new.html",
            context=dict,
        )

    def post(self, request):
        hero_class = Classes.objects.filter(name=request.POST.get("class"))
        race = Races.objects.filter(name=request.POST.get("race"))
        alignment = Alignments.objects.filter(name=request.POST.get("alignment"))

        CHECKBOX_MAPPING = {'on': True,
                            'off': False, }

        Character.objects.create(
            # BASIC INFO
            name=request.POST.get("charname"),
            basic_level=request.POST.get("level"),
            experience=request.POST.get("experiencepoints"),
            race=race[0],
            alignment=alignment[0],
            background=request.POST.get("background"),
            player=request.user,
            # MAIN STATS
            strength=int(request.POST.get("Strengthscore")),
            strength_mod=int(request.POST.get("Strengthmod")),
            dexterity=int(request.POST.get("Dexterityscore")),
            dexterity_mod=int(request.POST.get("Dexteritymod")),
            constitution=int(request.POST.get("Constitutionscore")),
            constitution_mod=int(request.POST.get("Constitutionmod")),
            wisdom=int(request.POST.get("Wisdomscore")),
            wisdom_mod=int(request.POST.get("Wisdommod")),
            intelligence=int(request.POST.get("Intelligencescore")),
            intelligence_mod=int(request.POST.get("Intelligencemod")),
            charisma=int(request.POST.get("Charismascore")),
            charisma_mod=int(request.POST.get("Charismamod")),
            # SAVING THROWS
            strength_save_prof=bool(CHECKBOX_MAPPING.get(request.POST.get("Strength-save-prof"))),
            dexterity_save_prof=bool(CHECKBOX_MAPPING.get(request.POST.get("Dexterity-save-prof"))),
            constitution_save_prof=bool(CHECKBOX_MAPPING.get(request.POST.get("Constitution-save-prof"))),
            wisdom_save_prof=bool(CHECKBOX_MAPPING.get(request.POST.get("Wisdom-save-prof"))),
            intelligence_save_prof=bool(CHECKBOX_MAPPING.get(request.POST.get("Intelligence-save-prof"))),
            charisma_save_prof=bool(CHECKBOX_MAPPING.get(request.POST.get("Charisma-save-prof"))),
            # PROFICIENCIES
            proficiency_bonus=int(request.POST.get("proficiencybonus")),
            acrobatics_prof=bool(CHECKBOX_MAPPING.get(request.POST.get("Acrobatics-prof"))),
            animal_handling_prof=bool(CHECKBOX_MAPPING.get(request.POST.get("Animal Handling-prof"))),
            arcana_prof=bool(CHECKBOX_MAPPING.get(request.POST.get("Arcana-prof"))),
            athletics_prof=bool(CHECKBOX_MAPPING.get(request.POST.get("Athletics-prof"))),
            deception_prof=bool(CHECKBOX_MAPPING.get(request.POST.get("Deception-prof"))),
            history_prof=bool(CHECKBOX_MAPPING.get(request.POST.get("History-prof"))),
            insight_prof=bool(CHECKBOX_MAPPING.get(request.POST.get("Insight-prof"))),
            intimidation_prof=bool(CHECKBOX_MAPPING.get(request.POST.get("Intimidation-prof"))),
            investigation_prof=bool(CHECKBOX_MAPPING.get(request.POST.get("Investigation-prof"))),
            medicine_prof=bool(CHECKBOX_MAPPING.get(request.POST.get("Medicine-prof"))),
            nature_prof=bool(CHECKBOX_MAPPING.get(request.POST.get("Nature-prof"))),
            perception_prof=bool(CHECKBOX_MAPPING.get(request.POST.get("Perception-prof"))),
            performance_prof=bool(CHECKBOX_MAPPING.get(request.POST.get("Performance-prof"))),
            persuasion_prof=bool(CHECKBOX_MAPPING.get(request.POST.get("Persuasion-prof"))),
            religion_prof=bool(CHECKBOX_MAPPING.get(request.POST.get("Religion-prof"))),
            sleight_of_hand_prof=bool(CHECKBOX_MAPPING.get(request.POST.get("Sleight of Hand-prof"))),
            stealth_prof=bool(CHECKBOX_MAPPING.get(request.POST.get("Stealth-prof"))),
            survival_prof=bool(CHECKBOX_MAPPING.get(request.POST.get("Survival-prof"))),
            passive_perception=int(request.POST.get("passiveperception")),
            # COMBAT AND MOVEMENT
            armor_class=int(request.POST.get("ac")),
            speed=request.POST.get("speed"),
        )

        new_char = Character.objects.get(name=request.POST.get("charname"))
        new_char.hero_classes.set(hero_class)
        new_char.save()

        return HttpResponseRedirect(f'/view_character/{new_char.id}')


class AllHeroesListView(LoginRequiredMixin, ListView):
    model = Character
    ordering = "name"
    template_name = "char_app/char_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(player=self.request.user)


class HeroDetailView(LoginRequiredMixin, DetailView):
    model = Character
    pk_url_kwarg = 'id'
    template_name = "char_app/char_view.html"
