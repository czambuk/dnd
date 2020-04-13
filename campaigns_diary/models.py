from django.db import models
from char_app.models import Player, Character
# from django.contrib.auth.models import User


class Campaign(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    realm = models.CharField(max_length=64,
                             default='Forgotten Realms'
                             )
    characters = models.ManyToManyField(Character)

    def __str__(self):
        return self.name


class CampaignEntry(models.Model):
    entry_name = models.CharField(max_length=128)
    entry_content = models.TextField()
    time_added = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)
    chosen_campaign = models.ForeignKey("Campaign", on_delete=models.CASCADE)
