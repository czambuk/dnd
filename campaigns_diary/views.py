from django.shortcuts import redirect, get_object_or_404
from django.views import View

from .forms import (CampaignForm,
                    CampaignEntryForm
                    )

from .models import (Campaign,
                     CampaignEntry)

from django.views.generic import (CreateView,
                                  DeleteView,
                                  FormView,
                                  ListView,
                                  UpdateView
                                  )


class CampaignCreateView(CreateView):
    form_class = CampaignForm
    template_name = 'campaigns_diary/form.html'
    success_url = '/view_campaigns'

    def form_valid(self, form):
        Campaign.objects.create(**form.cleaned_data)
        return redirect('/view_campaigns')


class CampaignDeleteView(DeleteView):
    model = Campaign
    template_name = 'campaigns_diary/confirm_delete.html'
    pk_url_kwarg = 'campaign_id'

    def get_success_url(self):
        return '/view_campaigns'


class CampaignViewAllView(ListView):
    template_name = 'campaigns_diary/view_campaigns.html'
    model = Campaign


class CampaignEntryCreateView(CreateView):
    form_class = CampaignEntryForm
    template_name = 'campaigns_diary/form.html'
    success_url = '/view_campaigns'
    # TODO Dodać przekierowanie na stronę kampanii, dla której był dodawany wpis


class CampaignDetailView(ListView):
    template_name = 'campaigns_diary/list.html'
    model = CampaignEntry

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        chosen_campaign = Campaign.objects.get(id=self.kwargs['camp_id'])
        context['chosen_campaign'] = chosen_campaign

        entries = CampaignEntry.objects.filter(chosen_campaign_id=self.kwargs['camp_id'])
        context['entries'] = entries

        return context
