from django.shortcuts import render
from django.template.response import TemplateResponse
# from django.http import HttpResponse, HttpRequest
from django.views import View
from django import forms


class DiceRollForm(forms.Form):
    roll_data = forms.CharField(initial="i.e. 2k12+3")
    # roll_results = forms.CharField(
    #     widget=forms.Textarea
    # )
