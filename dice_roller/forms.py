from django import forms


class DiceRollForm(forms.Form):
    roll_data = forms.CharField(initial="i.e. 2k12+3", label="Kod rzutu")
