from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
                'username',
                'first_name',
                'last_name',
                'email')
        labels = {
                'username':'Usuario',
                'first_name' : 'Nombres',
                'last_name' : 'Apellidos',
                'email' : 'Correo',
        }
class MovieForm(forms.ModelForm):
    required_css_class = 'required'

    def __init__(self, *args, **kwargs):
        super(MovieForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget = forms.TextInput(attrs={'class': 'one'})
        self.fields['genre'].widget = forms.TextInput(attrs={'class': 'one'})
        self.fields['year'].widget = forms.DateInput(attrs={'class': 'one'})
        self.fields['director'].widget = forms.TextInput(attrs={'class': 'one'})


    class Meta:
        model = Movie
        fields = ["title", "genre","year","director"]
