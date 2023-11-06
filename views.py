from django.shortcuts import render

from django.http import HttpResponse 

from django.views import generic

from django.db import models
from django.urls import reverse 

from my_game_ranks.models import Game

from .forms import GameForm

from django.views.generic.edit import FormView

class GameListView(generic.ListView): 
      model = Game
      #def get_absolute_url(self): 
	   # return reverse('gamerank', args=[str(self.id)])

class GameDetailView(generic.DetailView): 
      model = Game 

class GameFormView(FormView):
    template_name = "game_form.html"
    form_class = GameForm
    success_url = "/thanks/"


def index(request): 



# Render the HTML template index.html with the data in the context variable. 

   #return HttpResponse('home page') 
   return render( request, 'my_game_ranks/index.html')