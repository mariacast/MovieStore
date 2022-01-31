from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView,CreateView,UpdateView,DeleteView, View
from .forms import *
from django.contrib.auth import authenticate
from django.urls import reverse_lazy
from .forms import *
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializer import*
from rest_framework.response import Response
from rest_framework.decorators import api_view

"""
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)


    return render(request,"login.html", {})"""

class UserRigister(CreateView):
    model = User
    template_name = 'UserRigister.html'
    form_class = RegisterForm
    success_url =reverse_lazy('RegistrarUsuario')

class MovieCreate(CreateView):

    model: Movie
    form_class = MovieForm
    template_name= 'MovieCreate.html'
    success_url = reverse_lazy('ListarPeliculas')

class MovieList(ListView):

    model = Movie
    template_name = 'MoviesShow.html'

class UserList(ListView):

    model = User
    template_name = 'UsersShow.html'

class MovieUpdate(UpdateView):
    model: Movie
    form_class = MovieForm
    queryset =Movie.objects.all()
    template_name= 'MovieUpdate.html'
    success_url = reverse_lazy('ListarPeliculas')

class UserUpdate(UpdateView):
    model: User
    form_class = RegisterForm
    queryset =User.objects.all()
    template_name= 'UserUpdate.html'
    success_url = reverse_lazy('ListarUsuarios')

class MovieDelete(DeleteView):
    model: Movie
    queryset =Movie.objects.all()
    success_url = reverse_lazy('ListarPeliculas')

#############
class MovieApiView(ModelViewSet):

    serializer_class =  MovieSerializer
    queryset = Movie.objects.all()
