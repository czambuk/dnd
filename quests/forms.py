from django import forms

from .models import (
    Quest,
    QuestStage
)


class QuestForm(forms.ModelForm):
    class Meta:
        model = Quest
        fields = (
            'name',
            'description',
            'which_campaign',
            'characters',
        )
        widgets = {
            'name': forms.TextInput,
            'description': forms.Textarea,
            'which_campaign': forms.Select,
            'characters': forms.SelectMultiple,
        }
        labels = {
            'name': 'Nazwa zadania',
            'description': 'Opis zadania',
            'which_campaign': 'Kampania',
            'characters': 'Bohaterowie',
        }


# class CampaignEntryForm(forms.ModelForm):
#     class Meta:
#         model = CampaignEntry
#         fields = (
#             'entry_name',
#             'entry_content',
#         )
#         widgets = {
#             'entry_name': forms.TextInput,
#             'entry_content': forms.Textarea,
#         }
#         labels = {
#             'entry_name': 'Tytuł wpisu',
#             'entry_content': 'Treść',
#         }
