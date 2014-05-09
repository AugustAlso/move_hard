from django.http import HttpResponse
from django.template.response import TemplateResponse
from moves.models import Move, Game
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from moves.forms import MoveForm


class MoveView(View):
    @method_decorator(csrf_exempt) #CSRF = Cross Site Request Forgery
    def dispatch(self, *args, **kwargs):
        return super(MoveView, self).dispatch(*args, **kwargs)

    def _get_helper(self, request, form): 
        movelist = Move.objects.all()
        gamelist = Game.objects.all()
        context = {
            'movelist': movelist,
            'gamelist': gamelist,
            'form': form,
        }
        return TemplateResponse(request, 'moves/index.html', context)

    def post(self, request): 
        mf = MoveForm(request.POST)
        if mf.is_valid():
            mf.save()
        return self._get_helper(request, mf)

    def get(self, request): 
        return self._get_helper(request, MoveForm())
