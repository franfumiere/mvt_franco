from django.contrib import admin
from django.urls import path
from flia.views import * 

urlpatterns = [
    path('silvana/', Silvana,),
    path('fede/', Fede),
    path('lola/', Lola),
    path('amigos/', amigos),
    path('familia/', familia),
    path('trabajo/', trabajo),
    path('', inicio)
]