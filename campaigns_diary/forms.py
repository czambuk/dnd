from django import forms

from .models import (Campaign,
                     CampaignEntry
                     )


class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = (
            'name',
            'comment',
        )
        widgets = {
            'name': forms.TextInput,
            'comment': forms.Textarea,
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
