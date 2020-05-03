from django.shortcuts import render
from django.views import View
from .forms import DiceRollForm

from dice_roll import throw_decode, roll


class DiceRollView(View):
    def get(self, request):
        form = DiceRollForm()
        return render(request,
                      "dice_roller/dice_roller.html",
                      {'form': form})

    def post(self, request):
        form = DiceRollForm(request.POST)
        if form.is_valid():
            roll_code = form.cleaned_data['roll_data']
            roll_data = throw_decode(roll_code)
            result = f"""Rzucono {roll_data[0]} razy kością {roll_data[1]} z {roll_data[2]} modyfikatorem
                        i wypadło... {roll(roll_code)}"""
            return render(request,
                          "dice_roller/dice_roller.html",
                          {'form': form,
                           'result': result,
                           }
                          )
