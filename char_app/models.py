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
    hero_classes = models.ManyToManyField(Classes)
    basic_level = models.IntegerField(default=1)
    additional_level = models.IntegerField(null=True, default=None)
    experience = models.IntegerField(default=0)
    race = models.ForeignKey(Races, on_delete=models.CASCADE, default=1)
    alignment = models.ForeignKey(Alignments, on_delete=models.CASCADE, default=2)
    background = models.CharField(max_length=64, default='TBD')
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    # STATS
    strength = models.IntegerField(default=10)
    strength_mod = models.IntegerField(default=0)
    dexterity = models.IntegerField(default=10)
    dexterity_mod = models.IntegerField(default=0)
    constitution = models.IntegerField(default=10)
    constitution_mod = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=10)
    wisdom_mod = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=10)
    intelligence_mod = models.IntegerField(default=0)
    charisma = models.IntegerField(default=10)
    charisma_mod = models.IntegerField(default=0)
    proficiency_bonus = models.IntegerField(default=0)
    strength_save_prof = models.BooleanField(default=False)
    strength_save_mod = models.IntegerField(default=0)
    dexterity_save_prof = models.BooleanField(default=False)
    dexterity_save_mod = models.IntegerField(default=0)
    constitution_save_prof = models.BooleanField(default=False)
    constitution_save_mod = models.IntegerField(default=0)
    wisdom_save_prof = models.BooleanField(default=False)
    wisdom_save_mod = models.IntegerField(default=0)
    intelligence_save_prof = models.BooleanField(default=False)
    intelligence_save_mod = models.IntegerField(default=0)
    charisma_save_prof = models.BooleanField(default=False)
    charisma_save_mod = models.IntegerField(default=0)

    # TODO

    def __str__(self):
        return f'{self.name}, poziom {self.basic_level}'
