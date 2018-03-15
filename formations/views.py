from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django import forms

# Create your views here.

from django.views import generic
from generic.views import *
from .models import Departement, Formation, UE, Module, Enseignant, Parcours,Document, Evaluation
from entreprises.models import Entreprise, Contrat
from promotions.models import Promotion, Groupe, Affectation_Etudiant, Affectation_Enseignant

#############################

class FormationFilterForm(forms.Form):
    active = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'class' :"custom-control-input"}))

class FormationListView(generic.ListView):
    model = Formation

    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = FormationFilterForm(self.request.GET)
        if self.form.is_valid():
            if self.form.cleaned_data["active"]:
                queryset=queryset.filter(active=self.form.cleaned_data["active"])
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"]=self.form
        return context

class FormationDetailView(generic.DetailView):
    model = Formation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["entreprises"]=Entreprise.objects.filter(contrat__affectation__promotion__formation__pk__in=[self.object.pk]).distinct()
        return context

class Consigne_ProjetDetailView(AjaxableDetailMixin):
    model = Formation
    template_name="formations/consigne.html"
    html_id="consigne_detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"]=self.object.consigne_projet
        context["file"]=self.object.grille_projet
        return context

class Consigne_ContratDetailView(AjaxableDetailMixin):
    model = Formation
    template_name="formations/consigne.html"
    html_id="consigne_detail"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"]=self.object.consigne_contrat
        context["file"]=self.object.grille_contrat
        return context

class Consigne_Feuille_EmargementDetailView(AjaxableDetailMixin):
    model = Formation
    template_name="formations/consigne.html"
    html_id="consigne_detail"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"]=self.object.consigne_feuille_emargement
        return context



class DepartementDetailView(AjaxableDetailMixin):
    model=Departement
    template_name="formations/departement_detail.html"


class FormationDetailView(AjaxableDetailMixin):
    model=Formation
    template_name="formations/formation_detail.html"



class UEDetailView(AjaxableDetailMixin):
    model=UE
    template_name="formations/ue_detail.html"


class ModuleDetailView(AjaxableDetailMixin):
    model=Module
    template_name="formations/module_detail.html"


class ParcoursDetailView(AjaxableDetailMixin):
    model=Parcours
    template_name="formations/parcours_detail.html"


## Enseignants

# AJAX
class EnseignantDetailView(AjaxableDetailMixin):
    model=Enseignant
    template_name="formations/enseignant_detail.html"

