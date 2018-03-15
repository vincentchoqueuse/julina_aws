from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from promotions.models import *
from entreprises.models import *
from generic.views import *
from .forms import *




# Contrat Detail

class ContratListView(ENSMixin,AdminListView):
    model = Contrat
    menu = "contrat"
    nav_active="entreprise"
    
    def get_queryset(self):
        entreprise=Contrat.objects.get(pk=self.kwargs["contrat"]).entreprise
        return Contrat.objects.filter(entreprise=entreprise)

class ContratDetailView(ENSMixin,AdminDetailView):
    model = Contrat
    menu= "contrat"
    pk_url_kwarg = "contrat"
    template_name="admin_ens/contrat_detail.html"
    nav_active="detail"

class EntrepriseDetailView(ENSMixin,AdminDetailView):
    model = Entreprise
    menu = "contrat"
    pk_url_kwarg = "contrat"
    detail_template="entreprises/entreprise_detail.html"

    def get_object(self, queryset=None):
        contrat=Contrat.objects.get(pk=self.kwargs["contrat"])
        return contrat.entreprise

class BulletinDetailView(ENSMixin,AdminDetailView):
    model = Bulletin
    menu = "contrat"
    pk_url_kwarg = "contrat"
    detail_template="promotions/bulletin_detail.html"

    def get_object(self, queryset=None):
        contrat=Contrat.objects.get(pk=self.kwargs["contrat"])
        return contrat.affectation.bulletin

class Fiche_LiaisonDetailView(ENSMixin,AdminDetailView):
    model = Fiche_Liaison
    menu = "contrat"
    
    def get_object(self, queryset=None):
        contrat=Contrat.objects.get(pk=self.kwargs["contrat"])
        return contrat.fiche_liaison

class Fiche_LiaisonUpdateView(ENSMixin,AjaxableUpdateMixin):
    model=Fiche_Liaison
    fields=["fonction_tuteur","telephone_tuteur","intitule","adresse_stage","service","programme","impression","dates_visite","problemes"]

    def get_object(self, queryset=None):
        contrat=Contrat.objects.get(pk=self.kwargs["contrat"])
        return contrat.fiche_liaison

class CalendrierDetailView(ENSMixin,AdminListView):
    model = Calendrier_Hebdomadaire
    menu = "contrat"
    nav_active="calendrier"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(affectation__promotion=self.kwargs["promotion"])


    def get_queryset(self):
        contrat = Contrat.objects.get(pk=self.kwargs["contrat"])
        return Calendrier_Hebdomadaire.objects.filter(calendrier__groupe__affectations=contrat.affectation)
    

# Consigne
class ConsigneDetailView(ENSMixin,AdminDetailView):
    can_update=False
    model = Contrat
    pk_url_kwarg = "contrat"
    menu="contrat"
    detail_template="formations/consigne_contrat_detail.html"
    nav_active="consigne"
    title="Détail Consigne"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"]=self.object.affectation.promotion.formation
        return context


class Rapport_Tuteur_FormationCreateView(ENSMixin,AjaxableCreateMixin):
    model=Rapport_Tuteur_Formation
    fields=["date_visite","condition_travail","integration","activite","visite","commentaires"]
    
    def form_valid(self, form):
        form.instance.contrat = get_object_or_404(Contrat,pk=self.kwargs['contrat'])
        return super().form_valid(form)

class Rapport_Tuteur_FormationUpdateView(ENSMixin,AjaxableUpdateMixin):
    model=Rapport_Tuteur_Formation
    fields=["date_visite","condition_travail","integration","activite","visite","commentaires"]

class Rapport_Tuteur_FormationDeleteView(ENSMixin,AjaxableDeleteMixin):
    model=Rapport_Tuteur_Formation



