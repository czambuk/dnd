from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
# from django.views import View
from django.contrib.auth.models import User

from .forms import (CampaignForm,
                    CampaignEntryForm
                    )

from .models import (Campaign,
                     CampaignEntry)

from char_app.models import Character

from django.views.generic import (CreateView,
                                  DeleteView,
                                  FormView,
                                  ListView,
                                  UpdateView
                                  )


class CampaignCreateView(LoginRequiredMixin, CreateView):
    form_class = CampaignForm
    template_name = 'landing_page/form.html'

    def form_valid(self, form):
        characters = form.cleaned_data['characters']
        del form.cleaned_data['characters']
        new_campaign = Campaign.objects.create(**form.cleaned_data)
        for char in characters:
            new_campaign.characters.add(Character.objects.get(id=char.id))
        return redirect(f'/view_campaigns/{new_campaign.id}')


class CampaignUpdateView(LoginRequiredMixin, UpdateView):
    model = Campaign
    form_class = CampaignForm
    template_name = 'landing_page/form.html'
    pk_url_kwarg = 'campaign_id'

    def get_success_url(self):
        return f'/view_campaigns/{self.object.id}'


class CampaignDeleteView(LoginRequiredMixin, DeleteView):
    model = Campaign
    template_name = 'campaigns_diary/confirm_delete.html'
    pk_url_kwarg = 'campaign_id'
    success_url = '/view_campaigns'


class CampaignViewAllView(LoginRequiredMixin, ListView):
    template_name = 'campaigns_diary/view_campaigns.html'
    model = Campaign

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)


class CampaignEntryCreateView(LoginRequiredMixin, CreateView):
    form_class = CampaignEntryForm
    template_name = 'landing_page/form.html'

    def get_success_url(self):
        return f'/view_campaigns/{self.object.chosen_campaign.id}'


class CampaignDetailView(LoginRequiredMixin, ListView):
    template_name = 'campaigns_diary/journal_list.html'
    model = CampaignEntry

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # Campaign object from db with id from URL
        chosen_campaign = Campaign.objects.get(id=self.kwargs['camp_id'])
        context['chosen_campaign'] = chosen_campaign
        # All CampaignEntry objects from db with campaign id from URL
        entries = CampaignEntry.objects.filter(chosen_campaign_id=self.kwargs['camp_id'])
        context['entries'] = entries

        return context
