from django.shortcuts import render

from django.http import HttpResponse 
from django.http import HttpResponseRedirect

from django.views import generic

from django.db import models
from django.urls import reverse 

from my_game_ranks.models import Game

from .forms import GameForm

from django.views.generic.edit import FormView

from django.shortcuts import redirect

from django.views.generic.edit import UpdateView 

class GameListView(generic.ListView): 
      model = Game
      #def get_absolute_url(self): 
	   # return reverse('gamerank', args=[str(self.id)])

class GameDetailView(generic.DetailView): 
      model = Game 

class GameFormView(FormView):
    template_name = "my_game_ranks/game_form.html"
    form_class = GameForm
    success_url = "/gamerank/"

class UpdateGameView(UpdateView):
    template_name = "my_game_ranks/update_game_form.html"
    model= Game
    fields = ["title","picture","ranking"]
    success_url = "/gamerank/"

def index(request): 
# Render the HTML template index.html with the data in the context variable. 
   #return HttpResponse('home page') 
    return render( request, 'my_game_ranks/index.html')


def create_game(request):

    if request.method == "POST":

        form = GameForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("gamerank/")

    else:
        form = GameForm()

    return render(request, "my_game_ranks/game_form.html", {"form": form})




def edit_game(request,game_id):
        game = Game.objects.get(pk=game_id)
        game.save()
        return render(request, "my_game_ranks/update_game_form.html", {"form": form})



    