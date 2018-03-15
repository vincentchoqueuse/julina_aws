
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404

from promotions.models import Promotion, Groupe, Etudiant, Affectation_Etudiant, Affectation_Enseignant, Calendrier
from formations.models import Document4Groupe
from generic.views import *
from entreprises.models import Contrat, Fiche_Liaison
from projets.models import Projet_Tuteure, Suivi_Projet

from django.contrib.auth.mixins import UserPassesTestMixin


BASE_TEMPLATE_NAME="admin_etu"

class ETUMixin(UserPassesTestMixin):
    
    login_url = "/login/"
    url_prefix="admin_etu"
    
    def test_func(self):
        if hasattr(self.request.user, 'etudiant'):
            output=True
        else:
            output=False
        return output

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["is_etu"]=True
        return context

##### MENU ETUDIANT

class EtudiantDetailView(ETUMixin,AdminDetailView):
    model = Etudiant
    template_name="admin_etu/index.html"
    
    def get_object(self, queryset=None):
        return self.request.user.etudiant


class EtudiantUpdateView(ETUMixin,AjaxableUpdateMixin):
    model=Etudiant
    fields =  ["email_perso","domicile","villedomicile","codepostaldomicile","telephone","telephonemobile","bac","bac2","annee_bac","annee_bac2"]
    
    def get_object(self, queryset=None):
        return self.request.user.etudiant

    def form_valid(self, form):
        self.object = form.save()
        html=render_to_string("admin_etu/etudiant_detail.html",{"object":self.object,},request=self.request,)
        return JsonResponse({"etudiant_detail":html})


##### MENU Affectation
class Affectation_EtudiantDetailView(ETUMixin,AdminDetailView):
    model = Affectation_Etudiant
    template_name="admin_etu/affectation_etudiant_detail.html"

class Affectation_EtudiantUpdateView(ETUMixin,AjaxableUpdateMixin):
    model=Affectation_Etudiant
    fields =  ["bulletin_visible"]
    
    def form_valid(self, form):
        self.object = form.save()
        if self.object.bulletin_visible==True:
            html="<i class='fa fa-unlock' aria-hidden='true'></i>"
        else:
            html="<i class='fa fa-lock' aria-hidden='true'></i>"
        return JsonResponse({"id":"bulletin_link","content":html})




##### MENU CONTRAT
class ContratDetailView(ETUMixin,AdminDetailView):
    model = Contrat
    template_name="admin_etu/contrat_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["etudiant"]=self.object.affectation.etudiant
        return context


class Fiche_LiaisonCreateView(ETUMixin,AjaxableCreateMixin):
    model=Fiche_Liaison
    fields=["fonction_tuteur","telephone_tuteur","intitule","adresse_stage","service","programme","impression","dates_visite","problemes"]
    
    def form_valid(self, form):
        form.instance.contrat = get_object_or_404(Contrat,pk=self.kwargs["contrat"])
        self.object = form.save()
        html=render_to_string("admin_etu/contrat_suivi_list.html",{"object":self.object.contrat,},request=self.request,)
        return JsonResponse({"contrat_suivi_table":html})

class Fiche_LiaisonUpdateView(ETUMixin,AjaxableUpdateMixin):
    model=Fiche_Liaison
    fields=["fonction_tuteur","telephone_tuteur","intitule","adresse_stage","service","programme","impression","dates_visite","problemes"]

    def form_valid(self, form):
        self.object = form.save()
        html=render_to_string("admin_etu/contrat_suivi_list.html",{"object":self.object.contrat,},request=self.request,)
        return JsonResponse({"contrat_suivi_table":html})


##### MENU PROJET TUTEURE
class Projet_TuteureDetailView(ETUMixin,AdminDetailView):
    model = Projet_Tuteure
    template_name="admin_etu/projet_tuteure_detail.html"


