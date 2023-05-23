from django.shortcuts import get_object_or_404, render, redirect
from .forms import *
from .models import *
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse


#service
def listSer(request):
    list=Service.objects.all()
    return render(request, 'service/affiche_service.html',{'list':list})

def AddService(request):
    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listSer')
    else:
        form = ServiceForm()
    service = Service.objects.all()
    return render(request, 'service/AddS.html', {'service': service, 'form': form})

def edit_Service(request, service_id):
    service = Service.objects.get(id=service_id)
    form = ServiceForm(instance=service)
    
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('listSer')
    
    return render(request, 'service/edit_service.html', {'form': form, 'service': service})

def view_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'service/service_detail.html', {'service': service})

def delete_service(request, service_id):
    # Récupérer le service correspondant à l'identifiant unique donné
    service = get_object_or_404(Service, id=service_id)

    if request.method == 'POST':
        # Supprimer le service de la base de données
        service.delete()
        return redirect('listSer')
    return render(request, 'service/delete_service.html', {'service': service})
#register
def register(request):
    if request.method == 'POST' :  
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('login')
    else :
        form = UserRegistrationForm()
    return render(request,'registration/register.html',{'form' : form})

#projet
def listprojet(request):
    listp=Projet.objects.all()
    return render(request, 'projet/affiche_projet.html',{'listp':listp})
def Addprojet(request):
    if request.method == "POST":
        form = ProjetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listprojet')
    else:
        form = ProjetForm()
    projet = Projet.objects.all()
    return render(request, 'projet/AddP.html', {'projet': projet, 'form': form})
def edit_projet(request, projet_id):
    projet = Projet.objects.get(id=projet_id)
    form = ProjetForm(instance=projet)
    
    if request.method == 'POST':
        form = ProjetForm(request.POST, instance=projet)
        if form.is_valid():
            form.save()
            return redirect('listprojet')
    
    return render(request, 'projet/edit_projet.html', {'form': form, 'projet': projet})
def view_projet(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    return render(request, 'projet/projet_detail.html', {'projet': projet})

def delete_projet(request, projet_id):
    # Récupérer le service correspondant à l'identifiant unique donné
    projet = get_object_or_404(Projet, id=projet_id)

    if request.method == 'POST':
        # Supprimer le service de la base de données
        projet.delete()
        return redirect('listprojet')
    return render(request, 'projet/delete_projet.html', {'projet': projet})


def projets_acheves(request):
    projets = Projet.objects.filter(acheve='o')
    return render(request, 'projet/affiche_acheve.html', {'projets': projets})

def projets_non_acheves(request):
    projets = Projet.objects.filter(acheve='n')
    return render(request, 'projet/affiche_nonacheve.html', {'projets': projets})
def release_equipe(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    if projet.acheve == 'o' and projet.equipe is not None:
        projet.equipe = None
        projet.save()
        # Additional logic or rendering if needed
        return render(request, 'projet/release_success.html')
    else:
        # Additional logic or rendering if needed
        return render(request, 'projet/release_failure.html')

#personnel
def listPerson(request):
    listpe=Personnel.objects.all()
    return render(request,'personnel/mesPersonnel.html',{'listpe':listpe})
def personnel_create(request):
    if request.method == 'POST':
        form = PersonnelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listPerson')
    else:
        form = PersonnelForm()
    personne=Personnel.objects.all()
    return render(request, 'personnel/addPersonnel.html', {'personne': personne,'form': form})
def personnel_edit(request,id):
    post = get_object_or_404(Personnel, id=id)
    if request.method == 'GET':
        context = {'form': PersonnelForm(instance=post), 'id': id}
        return render(request,'personnel/editPersonnel.html',context)
    elif request.method == 'POST':
        form = PersonnelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('listPerson')
        else:
            return render(request,'personnel/editPersonnel.html',{'form':form})        
def personnel_delete(request, id):
    personnel = get_object_or_404(Personnel, pk=id)
    context = {'personnel': personnel}    
    if request.method == 'GET':
        return render(request, 'personnel/deletePersonnel.html',context)
    elif request.method == 'POST':
        personnel.delete()
        return redirect('listPerson')
def view_personne(request, id):
    personnel = get_object_or_404(Personnel, id=id)
    return render(request, 'personnel/personnel_detail.html', {'personnel': personnel})
#equipe
def listequipe(request):
    listq=Equipe.objects.all()
    return render(request,'equipe/afficheequipe.html',{'listq':listq})

"""def create_equipe(nom, personnel_list):
    equipe = Equipe.objects.create(nom=nom)
    for personnel in personnel_list:
        equipe.personnel.add(personnel)
    equipe.save()
    return equipe"""
def equipe_create(request):
    if request.method == 'POST':
        form = EquipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listequipe')
    else:
        form = EquipeForm()
    equipe=Equipe.objects.all()
    return render(request, 'equipe/addequipe.html', {'equipe': equipe,'form': form})
def edit_team(request, team_id):
    team = get_object_or_404(Equipe, id=team_id)
    if request.method == 'POST':
        form = EquipeForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('listequipe')
    else:
        form = EquipeForm(instance=team)
    return render(request, 'equipe/edit_equipe.html', {'form': form})

def delete_team(request, team_id):
    team = get_object_or_404(Equipe, id=team_id)
    if request.method == 'POST':
        team.delete()
        return redirect('listequipe')
    return render(request, 'equipe/delete_equipe.html', {'team': team})
#contact
def contact(request):
     return render(request,'Contact/contact.html')

def send_email(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		message = request.POST.get('message')
		send_mail(
			subject,
			'Contact from ' + name + ' (' + email + ')\n\n' + message,
			email,
			['adamkhabou719@gmail.com'],
			fail_silently=False,
		)
		return render(request,'Contact/contact.html',{'name':name})
	return render(request, 'Contact/contact.html')

def projet_utilisateur_list(request):
    projetutilisateurs = ProjetUtilisateur.objects.filter(utilisateur=request.user)
    context = {'projetutilisateurs': projetutilisateurs}
    return render(request, 'projet utilisateur/projet_utilisateur_list.html', context)
def ajouter_projet_utilisateur(request):
    if request.method == 'POST':
        form = ProjetUtilisateurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projet_utilisateurlist')
    else:
        form = ProjetUtilisateurForm()
    return render(request, 'projet utilisateur/ajouter_projet_utilisateur.html', {'form': form})

def demandeproj(request):
     return render(request,'projet utilisateur/demande_projet.html')
from django.core.mail import send_mail

def send_emailproj(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        projname = request.POST.get('projname')
        description = request.POST.get('description')
        date_fin = request.POST.get('date_fin')
        imageproj = request.POST.get('imageproj')
        serviceproj = request.POST.get('serviceproj')
        
        send_mail(
            projname,
            'Contact from ' + name + ' (' + email + ')\n\n' + description +'\n date fin '+date_fin+'\n image '+imageproj+'\n service '+serviceproj,
            email,
            ['adamkhabou719@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'projet utilisateur/demande_projet.html', {'name': name})
    
    return render(request, 'projet utilisateur/demande_projet.html')
