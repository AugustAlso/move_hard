from django import forms
from moves.models import Game, Move

class MoveForm(forms.Form): 
    value = forms.CharField(max_length=140)
    game = forms.CharField(max_length=140)

    def save(self): 
        value = self.cleaned_data['value']
        game = self.cleaned_data['game']
        m = Move(value=value, game=game)
        m.save()
        return m

    def clean_game(self):
        game, created = Game.objects.get_or_create(title=self.cleaned_data['game'])
        return game
