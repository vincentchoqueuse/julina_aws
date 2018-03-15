from .models import *
from .forms import *
from generic.views import *
from entreprises.models import *
from projets.models import Projet_Tuteure
from promotions.models import Affectation_Enseignant

##### MENU ENSEIGNANT

class EnseignantDetailView(ENSMixin,AdminDetailView):
    model = Enseignant
    template_name="admin_ens/profil_index.html"
    menu="profil"
    
    def get_object(self, queryset=None):
        return self.request.user.enseignant

class EnseignantUpdateView(ENSMixin,AjaxableUpdateMixin):
    model=Enseignant
    fields =  ["photo","statut","employeur","email","telephonemobile","telephone","adresse_rue","adresse_zip","adresse_ville","contraintes"]
    
    def get_object(self, queryset=None):
        return self.request.user.enseignant


class Affectation_EnseignantListView(ENSMixin,AdminListView):
    model = Affectation_Enseignant
    menu="profil"
    can_filter="True"
    title="Liste des affectations"
    
    def get_queryset(self):
        queryset=Affectation_Enseignant.objects.filter(enseignant=self.request.user.enseignant)
        self.form = FilterForm(self.request.GET)
        if self.form.is_valid():
            if self.form.cleaned_data["actif"]==True:
                queryset=queryset.filter(groupe__promotion__active=True)
        return queryset


class Affectation_EnseignantUpdateView(ENSMixin,AjaxableUpdateMixin):
    model=Module
    fields=["objectifs","competences_minimales","pre_requis","contenu","modalites","mots_cles"]
    
    def get_object(self, queryset=None):
        affectation=Affectation_Enseignant.objects.get(pk=self.kwargs.get(self.pk_url_kwarg))
        return affectation.module



class ContratListView(ENSMixin,AdminListView):
    model = Contrat
    can_filter="True"
    menu="profil"
    title="Liste des contrats"

    def get_queryset(self):
        queryset = Contrat.objects.filter(tuteur_formation=self.request.user.enseignant)
        self.form = FilterForm(self.request.GET)
        if self.form.is_valid():
            if self.form.cleaned_data["actif"]==True:
                queryset=queryset.filter(affectation__promotion__active=True)
        return queryset


class Projet_TuteureListView(ENSMixin,AdminListView):
    model = Projet_Tuteure
    menu="profil"
    title="Liste des projets"
    
    def get_queryset(self):
        return Affectation_Enseignant.objects.filter(enseignant=self.request.user.enseignant)








