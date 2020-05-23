from django.contrib import admin
from .models import Races, Classes, Alignments, Character


@admin.register(Races)
class RacesAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


@admin.register(Alignments)
class AlignmentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'basic_level',
                    'alignment',
                    'race',
                    'player',
                    )

