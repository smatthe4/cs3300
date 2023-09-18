from . import views 
from django.urls import path , include

app_name = 'portfolio_app'

 
 

urlpatterns = [ 

#path function defines a url pattern 

#'' is empty to represent based path to app 

# views.index is the function defined in views.py 

# name='index' parameter is to dynamically create url 

# example in html <a href="{% url 'index' %}">Home</a>. 

path('', views.index, name='index'), ]