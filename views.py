from django.shortcuts import render

from django.http import HttpResponse 

from django.views import generic







def index(request): 



# Render the HTML template index.html with the data in the context variable. 

   #return HttpResponse('home page') 
   return render( request, 'my_game_ranks/index.html')