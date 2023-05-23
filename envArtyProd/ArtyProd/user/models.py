from datetime import date
from django.db import models

from django.contrib.auth.models import User

class Service (models.Model):
    TYPE_CHOICES=[
        ('cg','Charte graphique '),
        ('ob','Objet  3D'),
        ('Sc','Scénarisation')
    ]
    type=models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
    description=models.TextField(default='Non définie')

    def __str__(self):
        return "type "+self.type+" description "+self.description
class Personnel(models.Model):
    nom=models.CharField(max_length=100)
    fichier_CV=models.FileField(blank=True,upload_to='media/')
    fichier_photo=models.ImageField(blank=True,upload_to='media/')
    lien_linkedln = models.URLField()
    
    def __str__(self):
        return "nom"+self.nom
class detail(models.Model):
    fichier=models.FileField(blank=True,upload_to='media/')
    service=models.ForeignKey('Service',on_delete=models.CASCADE,null=True)
    projet=models.ForeignKey('Projet',on_delete=models.CASCADE,null=True)
class Projet(models.Model):
    TYPE_CHOICES=[
        ('o','oui'),
        ('n','non'),
    ]
    libellé=models.CharField(max_length=100)
    description=models.TextField(default='Non définie')
    date_debut = models.DateField()
    date_fin = models.DateField()
    acheve=models.CharField(max_length=1,choices=TYPE_CHOICES,default='n')
    img=models.ImageField(blank=True,upload_to='media/')
    service=models.ManyToManyField('Service',through="detail")
    equipe=models.OneToOneField('Equipe',on_delete=models.CASCADE,null=True)
    def save(self, *args, **kwargs):
        if self.acheve == 'o' and self.equipe is not None:
            self.equipe = None
        super().save(*args, **kwargs)
class Equipe(models.Model):
    nom=models.CharField(default='non définie',max_length=100)
    personnels=models.ManyToManyField('Personnel')
    def __str__(self):
        personnel_list = ", ".join(personnel.nom for personnel in self.personnels.all())
        i=self.id
        return f"Equipe {i} : ({personnel_list})"
class ProjetUtilisateur(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    projet = models.ManyToManyField(Projet)

    def __str__(self):
        return " "+self.projet.libellé  +" "+str(self.projet.date_fin)+" "+str(self.utilisateur.username)
# class User(AbstractUser):
#     nom=models.CharField(max_length=100)
#     fichier_photo = models.FileField()
