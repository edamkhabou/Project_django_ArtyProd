from django import forms

from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
class ServiceForm (ModelForm):
    class Meta :
        model = Service
        fields = "__all__"
class ProjetForm (ModelForm):
    class Meta :
        model = Projet
        fields = "__all__"
class ProjectFormR(ModelForm):
    class Meta:
        model=Projet
        fields=['acheve']
class PersonnelForm (ModelForm):
    class Meta :
        model = Personnel
        fields = "__all__"
class EquipeForm (ModelForm):
    class Meta :
        model = Equipe
        fields = "__all__"
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')
class EquipeForm (ModelForm):
    class Meta :
        model = Equipe
        fields = "__all__"
class ProjetUtilisateurForm(forms.ModelForm):
    projet = forms.ModelMultipleChoiceField(queryset=Projet.objects.filter(date_debut=date.today()), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = ProjetUtilisateur

        fields = "__all__"