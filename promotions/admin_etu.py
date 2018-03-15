from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import *
from generic.views import *
from entreprises.models import *
from projets.models import *
from promotions.models import *
from formations.models import *

class EtudiantDetailView(ETUMixin,AdminDetailView):
    model = Etudiant
    template_name="admin_etu/profil_detail.html"
    menu="profil"
    nav_active="detail"
    
    def get_object(self, queryset=None):
        return self.request.user.etudiant

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projet_tuteure_list"]=Projet_Tuteure.objects.filter(affectation__etudiant=self.object)
        context["contrat_list"]=Contrat.objects.filter(affectation__etudiant=self.object)
        context["affectation_etudiant_list"]=Affectation_Etudiant.objects.filter(etudiant=self.object)
        return context





class EtudiantUpdateView(ETUMixin,AjaxableUpdateMixin):
    model=Etudiant
    fields =  ["email_perso","domicile","villedomicile","codepostaldomicile","telephone","telephonemobile","bac","bac2","annee_bac","annee_bac2"]
    
    def get_object(self, queryset=None):
        return self.request.user.etudiant
    
    def form_valid(self, form):
        self.object = form.save()
        html=render_to_string("admin_etu/etudiant_detail.html",{"object":self.object,},request=self.request,)
        return JsonResponse({"etudiant_detail":html})


class CalendrierListView(ETUMixin,AdminListView):
    model=Calendrier_Hebdomadaire
    template_name="admin_etu/profil_calendrier.html"
    title="Calendrier"
    menu="profil"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(calendrier__groupe__affectations__etudiant=self.request.user.etudiant)


class Affectation_EtudiantDetailView(ETUMixin,AdminDetailView):
    model = Affectation_Etudiant
    template_name="admin_etu/affectation_etudiant_detail.html"
    pk_url_kwarg = "affectation_etudiant"
    menu="affectation_etudiant"
    nav_active="detail"


class Affectation_EtudiantUpdateView(ETUMixin,AjaxableUpdateMixin):
    model=Affectation_Etudiant
    fields =  ["bulletin_visible"]
    pk_url_kwarg = "affectation_etudiant"

class DocumentListView(ETUMixin,AdminListView):
    model=Document4Groupe
    title="Liste des Documents"
    menu="affectation_etudiant"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(affectation_enseignant__groupe__affectations=self.kwargs["affectation_etudiant"])

class EnseignantListView(ETUMixin,AdminListView):
    model=Affectation_Enseignant
    menu="affectation_etudiant"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(groupe__affectations=self.kwargs["affectation_etudiant"]).distinct()

class EtudiantListView(ETUMixin,AdminListView):
    model=Affectation_Etudiant
    menu="affectation_etudiant"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(groupe__affectations=self.kwargs["affectation_etudiant"]).distinct()

class Projet_TuteureListView(ETUMixin,AdminListView):
    model=Projet_Tuteure
    menu="affectation_etudiant"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        affectation_etudiant=Affectation_Etudiant.objects.get(pk=self.kwargs["affectation_etudiant"])
        return queryset.filter(promotion=affectation_etudiant.promotion).distinct()

class Calendrier2ListView(ETUMixin,AdminListView):
    model=Calendrier_Hebdomadaire
    menu="affectation_etudiant"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(calendrier__groupe__affectations=self.kwargs["affectation_etudiant"])



    
