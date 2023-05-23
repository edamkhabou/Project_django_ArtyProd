from django.contrib import admin
from .models import detail
from .models import Projet
from .models import Equipe
from .models import Personnel
from .models import Service
from .models import ProjetUtilisateur
admin.site.register(detail)
admin.site.register(Projet)
admin.site.register(Equipe)
admin.site.register(Personnel)
admin.site.register(Service)
admin.site.register(ProjetUtilisateur)
