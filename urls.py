from . import views 
from django.db import models
from django.urls import reverse 
from django.urls import path , include

app_name = 'my_game_ranks'




"""
URL configuration for my_game_ranks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('gamerank/', views.GameListView.as_view(), name='gamerank'),
    path('game/<int:pk>/', views.GameDetailView.as_view(), name='gamedetail'),
    path('create_game/', views.GameFormView.as_view(), name='create_game'),

    path('<int:pk>/edit_game', views.UpdateGameView.as_view(), name='edit_game'),

    path('<int:pk>/delete', views.Delete.as_view(), name='delete'),

    path('postgame', views.create_game, name='post_game'),

    path('signup', views.signup, name='signup'),

    path('login_view', views.login_view, name='login_view'),

    path('logout_view', views.logout_view, name='logout_view'),

    path('sorttest', views.sorttest, name='sorttest'),

    
]
