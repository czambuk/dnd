from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=128, null=False)


class Character(models.Model):
    # BASIC INFO
    name = models.CharField(max_length=64)
    basic_class = models.CharField(max_length=32)
    additional_class = models.CharField(max_length=32,
                                        null=True,
                                        default=None
                                        )
    basic_level = models.IntegerField()
    additional_level = models.IntegerField(null=True,
                                           default=None)
    experience = models.IntegerField(default=0)
    race = models.CharField(max_length=32)
    alignment = models.IntegerField(default=5)
    # TODO choices for alignment, 9 choices
    background = models.CharField(max_length=64, default='TBD')
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    # STATS

