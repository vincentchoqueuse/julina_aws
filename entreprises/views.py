from django.shortcuts import render
from django.views import generic
from .models import *
from formations.models import *
from promotions.models import *
from entreprises.models import *
from projets.models import *
from generic.views import *
from django import forms
from django.http import JsonResponse



#form


# Create your views here.


###### AJAX



class Rapport_Tuteur_FormationDetailView(AjaxableDetailMixin):
    model=Rapport_Tuteur_Formation
    template_name="entreprises/rapport_tuteur_formation_detail.html"

class Rapport_Tuteur_EntrepriseDetailView(AjaxableDetailMixin):
    model=Rapport_Tuteur_Entreprise
    template_name="entreprises/rapport_tuteur_entreprise_detail.html"

class Fiche_LiaisonDetailView(AjaxableDetailMixin):
    model=Fiche_Liaison
    template_name="entreprises/fiche_liaison_detail.html"

class ContratDetailView(AjaxableDetailMixin):
    model=Contrat
    template_name="entreprises/contrat_detail.html"




# AJAX

class EntrepriseDetailView(AjaxableDetailMixin):
    model=Entreprise
    template_name="entreprises/entreprise_detail.html"

## Tuteurs




# AJAX
class TuteurDetailView(AjaxableDetailMixin):
    model=Tuteur_Entreprise
    template_name="entreprises/tuteur_detail.html"

# Standard


#### LIST
def entreprise_list(request):
    entreprises=Entreprise.objects.all().values_list('nom',flat=True)
    entreprise_list = list(entreprises)
    return JsonResponse(entreprise_list,safe=False)

