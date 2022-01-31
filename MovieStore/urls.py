
from django.contrib import admin
from Movies.views import *
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate


router= DefaultRouter()
router.register('MovieApiView', MovieApiView)


urlpatterns = [

    url('api/', include(router.urls)),
    #url('RegistrarUsuario/', UserRigister.as_view(),name="RegistrarUsuario"),
    #url('login/', login_view,name="login"),
    url('RegistrarUsuario/', UserRigister.as_view(),name="RegistrarUsuario"),
    #url('accounts/', include('django.contrib.auth.urls'))
    #url('login/', login, {'template_name':'registration/login.html'}, name='login'),
    url('login/', auth_views.LoginView.as_view(template_name='login.html')),
    url('logout/', auth_views.LogoutView.as_view(template_name='login.html')),
    url('CrearPelicula/', login_required(MovieCreate.as_view()),name="CrearPelicula"),
    url('ListarPeliculas/', login_required(MovieList.as_view()),name="ListarPeliculas"),
    url('ListarUsuarios/', login_required(UserList.as_view()),name="ListarUsuarios"),
    url(r'^ActualizarPelicula/(?P<pk>\d+)$', login_required(MovieUpdate.as_view()),name="ActualizarPelicula"),
    url(r'^EliminarPelicula/(?P<pk>\d+)$', login_required(MovieDelete.as_view()),name="EliminarPelicula"),
    url(r'^ActualizarUsuario/(?P<pk>\d+)$', login_required(UserUpdate.as_view()),name="ActualizarUsuario"),
]
