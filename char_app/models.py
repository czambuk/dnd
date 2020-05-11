from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=128)
    comment = models.TextField(null=True, default=None)

    def __str__(self):
        return self.name


class Character(models.Model):
    # BASIC INFO
    name = models.CharField(max_length=64)
    # TODO ManyToMany class relation
    basic_class = models.CharField(max_length=32)
    additional_class = models.CharField(max_length=32, null=True, default=None)
    basic_level = models.IntegerField(default=1)
    additional_level = models.IntegerField(null=True, default=None)
    experience = models.IntegerField(default=0)
    # TODO ManyToMany race relation
    race = models.CharField(max_length=32)
    alignment = models.IntegerField(default=5)
    # TODO choices for alignment, 9 choices
    background = models.CharField(max_length=64, default='TBD')
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    # TODO

    def __str__(self):
        return self.name
