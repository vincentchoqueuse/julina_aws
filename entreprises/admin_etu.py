from django.shortcuts import render, get_object_or_404
from .models import *
from generic.views import *
from entreprises.models import *
from projets.models import *
from promotions.models import *
from formations.models import *

class ContratDetailView(ETUMixin,AdminDetailView):
    model = Contrat
    template_name="admin_etu/contrat_detail.html"
    pk_url_kwarg = "contrat"
    menu="contrat"
    nav_active="detail"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class EntrepriseDetailView(ETUMixin,AdminDetailView):
    model=Entreprise
    pk_url_kwarg = "contrat"
    menu="entreprise"
    template_name="admin_etu/contrat_entreprise.html"
    nav_template="admin_etu/contrat_nav.html"
    title="Entreprise"
    nav_active="entreprise"
    
    
    def get_object(self, queryset=None):
        contrat=Contrat.objects.get(pk=self.kwargs["contrat"])
        return contrat.entreprise

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contrat_list"]=Contrat.objects.filter(entreprise=self.object)
        return context


class Fiche_LiaisonCreateView(ETUMixin,AjaxableCreateMixin):
    model=Fiche_Liaison
    fields=["fonction_tuteur","telephone_tuteur","intitule","adresse_stage","service","programme","impression","dates_visite","problemes"]
    
    def form_valid(self, form):
        form.instance.contrat = get_object_or_404(Contrat,pk=self.kwargs["contrat"])
        self.object = form.save()
        return super().form_valid(form)

class Fiche_LiaisonUpdateView(ETUMixin,AjaxableUpdateMixin):
    model=Fiche_Liaison
    fields=["fonction_tuteur","telephone_tuteur","intitule","adresse_stage","service","programme","impression","dates_visite","problemes"]
    
    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)


class ConsigneContratDetailView(ETUMixin,AdminDetailView):
    model=Contrat
    pk_url_kwarg = "contrat"
    detail_template="formations/consigne_contrat_detail.html"
    nav_active="consigne"
    menu="contrat"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"]=self.object.affectation.promotion.formation
        return context


