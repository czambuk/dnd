from django.db import models
# from django.contrib.auth.models import User


class Campaign(models.Model):
    name = models.CharField(max_length=128)
    comment = models.TextField()

    def __str__(self):
        return self.name


class CampaignEntry(models.Model):
    entry_name = models.CharField(max_length=128)
    entry_content = models.TextField()
    time_added = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)
    chosen_campaign = models.ForeignKey("Campaign", on_delete=models.CASCADE)
