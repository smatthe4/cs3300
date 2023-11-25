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


def index(request): 
# Render the HTML template index.html with the data in the context variable. 
   #return HttpResponse('home page') 
    return render( request, 'my_game_ranks/index.html')


def create_game(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = GameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect("gamerank/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GameForm()

    return render(request, "my_game_ranks/game_form.html", {"form": form})