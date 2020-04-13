from django import forms

from .models import (Campaign,
                     CampaignEntry
                     )


class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = (
            'name',
            'description',
            'realm',
            'characters',
        )
        widgets = {
            'name': forms.TextInput,
            'description': forms.Textarea,
            'characters': forms.SelectMultiple,
        }


class CampaignEntryForm(forms.ModelForm):
    class Meta:
        model = CampaignEntry
        fields = (
            'entry_name',
            'entry_content',
            'chosen_campaign',
        )
        widgets = {
            'entry_name': forms.TextInput,
            'entry_content': forms.Textarea,
            'chosen_campaign': forms.Select,
        }
