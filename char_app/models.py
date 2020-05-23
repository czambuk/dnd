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
    # BASIC STATS
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
    # SAVING THROWS
    strength_save_prof = models.BooleanField(default=False)
    dexterity_save_prof = models.BooleanField(default=False)
    constitution_save_prof = models.BooleanField(default=False)
    wisdom_save_prof = models.BooleanField(default=False)
    intelligence_save_prof = models.BooleanField(default=False)
    charisma_save_prof = models.BooleanField(default=False)
    # PROFICIENCIES
    proficiency_bonus = models.IntegerField(default=0)
    acrobatics_prof = models.BooleanField(default=False)
    animal_handling_prof = models.BooleanField(default=False)
    arcana_prof = models.BooleanField(default=False)
    athletics_prof = models.BooleanField(default=False)
    deception_prof = models.BooleanField(default=False)
    history_prof = models.BooleanField(default=False)
    insight_prof = models.BooleanField(default=False)
    intimidation_prof = models.BooleanField(default=False)
    investigation_prof = models.BooleanField(default=False)
    medicine_prof = models.BooleanField(default=False)
    nature_prof = models.BooleanField(default=False)
    perception_prof = models.BooleanField(default=False)
    performance_prof = models.BooleanField(default=False)
    persuasion_prof = models.BooleanField(default=False)
    religion_prof = models.BooleanField(default=False)
    sleight_of_hand_prof = models.BooleanField(default=False)
    stealth_prof = models.BooleanField(default=False)
    survival_prof = models.BooleanField(default=False)
    passive_perception = models.IntegerField(default=0)
    # COMBAT AND MOVEMENT
    armor_class = models.IntegerField(default=10)
    speed = models.DecimalField(max_digits=3, decimal_places=1, default=9)

    # TODO

    def __str__(self):
        return f'{self.name}, poziom {self.basic_level}'
