from django.shortcuts import render

from django.http import HttpResponse 

from django.views import generic

from django.db import models
from django.urls import reverse 

from my_game_ranks.models import Game
class GameListView(generic.ListView): 
      model = Game
      #def get_absolute_url(self): 
	   # return reverse('gamerank', args=[str(self.id)])





def index(request): 



# Render the HTML template index.html with the data in the context variable. 

   #return HttpResponse('home page') 
   return render( request, 'my_game_ranks/index.html')