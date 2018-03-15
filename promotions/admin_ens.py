from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import *
from formations.models import *
from generic.views import *
from projets.views import *
from entreprises.models import *

##### MENU PROMOTION

class PromotionDetailView(ENSMixin,AdminDetailView):
    model = Promotion
    pk_url_kwarg = "promotion"
    menu = "promotion"
    template_name="admin_ens/promotion_detail.html"
    

class MaquetteListView(ENSMixin,AdminListView):
    model = UE
    menu = "promotion"
    title="Liste des Modules"
    nav_active="formation"
    can_update=False
    can_delete=False
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(formation__promotion=self.kwargs["promotion"])


class Affectation_EtudiantListView(ENSMixin,AdminListView):
    model = Affectation_Etudiant
    menu = "promotion"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(promotion=self.kwargs["promotion"])

class EmargementListView(ENSMixin,AdminListView):
    
    model = Calendrier_Hebdomadaire
    menu = "promotion"
    nav_active="emargement"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(calendrier__promotion=self.kwargs["promotion"])

# Contrat

class ContratListView(ENSMixin,AdminListView):
    model = Contrat
    menu = "promotion"
    can_update=False
    can_delete=False
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(affectation__promotion=self.kwargs["promotion"])

# Projet

class Projet_TuteureListView(ENSMixin,AdminListView):
    model = Projet_Tuteure
    menu = "promotion"
    can_update=False
    can_delete=False
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(affectation__promotion=self.kwargs["promotion"]).distinct()


# Absence

class AbsenceListView(ENSMixin,AdminListView):
    
    model = Absence
    menu = "promotion"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(affectation_etudiant__promotion=self.kwargs["promotion"])

class AbsenceCreateView(ENSMixin,AjaxableCreateMixin):
    model=Absence
    fields=["affectation_etudiant","debut","fin","commentaire_ens"]
    
    def form_valid(self, form):
        self.object = form.save()
        self.object.enseignants.add(self.request.user.enseignant)
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["affectation_etudiant"].queryset = form.fields["affectation_etudiant"].queryset.filter(promotion__pk=self.kwargs["promotion"])
        return form

class AbsenceUpdateView(ENSMixin,AjaxableUpdateMixin):
    model=Absence
    fields=["debut","fin","commentaire_ens"]

class AbsenceDeleteView(ENSMixin,AjaxableDeleteMixin):
    model=Absence

class Document4GroupeListView(ENSMixin,AdminListView):
    
    model=Document4Groupe
    menu = "promotion"
    title="Liste des Documents"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(affectation_enseignant__groupe__promotion=self.kwargs["promotion"]).distinct()



class Document4GroupeCreateView(ENSMixin,AjaxableCreateMixin):
    model=Document4Groupe
    fields=["affectation_enseignant","nom","file"]
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["affectation_enseignant"].queryset = form.fields["affectation_enseignant"].queryset.filter(enseignant=self.request.user.enseignant,groupe__promotion__pk=self.kwargs["promotion"])
        return form


class Document4GroupeUpdateView(ENSMixin,AjaxableUpdateMixin):
    model=Document4Groupe
    fields=["affectation_enseignant","nom","file"]
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['affectation_enseignant'].queryset = form.fields['affectation_enseignant'].queryset.filter(enseignant=self.object.affectation_enseignant.enseignant,groupe__promotion__active=True)
        return form

class Document4GroupeDeleteView(ENSMixin,AjaxableDeleteMixin):
    model=Document4Groupe
    url_prefix="admin_ens"








