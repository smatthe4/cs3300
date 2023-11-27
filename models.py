from django.db import models
from django.urls import reverse 
#from django.contrib.auth.models import User


class Game(models.Model):
        title = models.CharField(max_length=200, blank=False) 
        picture = models.CharField("picture link", max_length=1000, blank=False)
        ranking = models.CharField(max_length=200)

        #user=models.ManyToManyField(User, verbose_name=("games"))



def get_absolute_url(self):
        return reverse('gamedetail', args=[str(self.id)])

#test comment