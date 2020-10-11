from django.db import models
from char_app.models import Character
from campaigns_diary.models import Campaign
from django.contrib.auth.models import User


class Quest(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    which_campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    characters = models.ManyToManyField(Character, blank=True)

    def __str__(self):
        return self.name


class QuestStage(models.Model):
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    which_quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
