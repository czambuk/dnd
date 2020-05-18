from django.db import models
from django.contrib.auth.models import User


class Races(models.Model):
    name = models.CharField(max_length=48)

    def __str__(self):
        return self.name


class Classes(models.Model):
    name = models.CharField(max_length=48)

    def __str__(self):
        return self.name


class Alignments(models.Model):
    name = models.CharField(max_length=48)

    def __str__(self):
        return self.name


class Character(models.Model):
    # BASIC INFO
    name = models.CharField(max_length=64)
    basic_class = models.ManyToManyField(Classes, related_name='basic_class')
    additional_class = models.ManyToManyField(Classes, related_name='additional_class')
    basic_level = models.IntegerField(default=1)
    additional_level = models.IntegerField(null=True, default=None)
    experience = models.IntegerField(default=0)
    race = models.ManyToManyField(Races)
    alignment = models.ManyToManyField(Alignments)
    background = models.CharField(max_length=64, default='TBD')
    player = models.ForeignKey(User, on_delete=models.CASCADE)

    # TODO

    def __str__(self):
        return f'{self.name}, {self.basic_class}, level {self.basic_level}'
