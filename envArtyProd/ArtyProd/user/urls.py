from django.urls import path,include
from . import views
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [	
    #service
    path('listSer/',views.listSer,name='listSer'),
    path('AddService/',views.AddService,name='AddService'),
    path('edit_Service/',views.edit_Service,name='edit_Service'),
    path('list/edit/<int:service_id>/', views.edit_Service, name='edit_Service'),
    path('view_service/',views.view_service,name='view_service'),
    path('list/<int:service_id>/view', views.view_service, name='view_service'),
    path('delete_service/',views.delete_service,name='delete_service'),
    path('list/<int:service_id>/Delete', views.delete_service, name='delete_service'),
    #register
    path('register/',views.register, name = 'register'), 
    #projet
    path('',views.listprojet,name='listprojet'),
    path('Addprojet/',views.Addprojet,name='Addprojet'),
    path('edit_projet/',views.edit_projet,name='edit_projet'),
    path('listp/edit/<int:projet_id>/', views.edit_projet, name='edit_projet'),
    path('view_projet/',views.view_projet,name='view_projet'),
    path('listp/<int:projet_id>/view', views.view_projet, name='view_projet'),
    path('delete_projet/',views.delete_projet,name='delete_projet'),
    path('listp/<int:projet_id>/DeleteProjet', views.delete_projet, name='delete_projet'),
    path('projets_acheves/', views.projets_acheves, name='projets_acheves'),
    path('projets_non_acheves/', views.projets_non_acheves, name='projets_non_acheves'),
    path('projet/release_equipe/<int:projet_id>/', views.release_equipe, name='release_equipe'),
    
    #personnel
    path('listPerson/',views.listPerson,name='listPerson'),
    path('personnel_create/',views.personnel_create,name='personnel_create'),
    path('personnel_edit/',views.personnel_edit,name='personnel_edit'),
    path('listpe/edit_personnel/<int:id>/', views.personnel_edit, name='personnel_edit'),
    path('personnel_delete/',views.personnel_delete,name='personnel_delete'),
    path('listpe/<int:id>/Delete_personnel', views.personnel_delete, name='personnel_delete'),
    path('view_personne/',views.view_personne,name='view_personne'),
    path('listpe/<int:id>/view_personnel', views.view_personne, name='view_personne'),

    #equipe
    path('listequipe/',views.listequipe,name='listequipe'),
    path('equipe_create/',views.equipe_create,name='equipe_create'),
    path('edit_team/',views.edit_team,name='edit_team'),
    path('delete_team/',views.delete_team,name='delete_team'),
    path('listq/<int:team_id>/edit', views.edit_team, name='edit_team'),
    path('listq/<int:team_id>/Delete', views.delete_team, name='delete_team'),
    #password-reset
    path('password-reset/', PasswordResetView.as_view(template_name='password_reset.html',html_email_template_name='password_reset_email.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    #contact
    path('contact/', views.contact, name='Contact'),
    path('send_mail/',views.send_email,name='send_email'),
    #ajouter project 
    path('projets/', views.projet_utilisateur_list, name='projet_utilisateurlist'),
    path('projetsajouter/', views.ajouter_projet_utilisateur, name='ajouterprojetutilisateur'),
    path('demandeprojet/',views.demandeproj,name='demandeproj'),
    path('send_emailproj/',views.send_emailproj,name='send_emailproj'),

    ]
