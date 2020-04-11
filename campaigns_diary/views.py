from django.shortcuts import redirect
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


class CampaignViewAllView(ListView):
    template_name = 'campaigns_diary/view_campaigns.html'
    model = Campaign


class CampaignDetailView(ListView):
    template_name = 'campaigns_diary/list.html'
    model = Campaign

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(**self.kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        chosen_campaign = Campaign.objects.get(id=self.kwargs['id'])
        context['chosen_campaign'] = chosen_campaign
        return context


