from django.contrib import admin
from .models import Campaign, CampaignEntry


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    pass


@admin.register(CampaignEntry)
class CampaignEntryAdmin(admin.ModelAdmin):
    pass
