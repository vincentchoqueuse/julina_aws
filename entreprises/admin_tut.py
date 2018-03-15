from .models import *
from generic.views import *
from projets.models import *
from promotions.models import *
from formations.models import *


class TuteurDetailView(TUTMixin,AdminDetailView):
    model = Tuteur_Entreprise
    template_name="admin_tut/profil_detail.html"
    menu="profil"
    nav_active="detail"
    
    def get_object(self, queryset=None):
        return self.request.user.tuteur_entreprise

class TuteurUpdateView(TUTMixin,AjaxableUpdateMixin):
    model = Tuteur_Entreprise
    fields =  ["nom","prenom","poste","email","telephonemobile","remarques"]
    
    def get_object(self, queryset=None):
        return self.request.user.tuteur_entreprise


class ContratDetailView(TUTMixin,AdminDetailView):
    model = Contrat
    template_name="admin_tut/contrat_detail.html"
    menu="contrat"
    nav_active="detail"


class Rapport_Tuteur_EntrepriseUpdateView(TUTMixin,AjaxableUpdateMixin):
    model = Rapport_Tuteur_Entreprise
    fields =  ["apprentissage","ecoute","curiosite","imagination","jugement","motivation","methode","autonomie","qualite","dynamisme","expression","relation","commentaire"]

class Rapport_Tuteur_FormationListView(TUTMixin,AdminListView):
    model = Rapport_Tuteur_Formation
    menu="contrat"
    nav_active="fiche"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(contrat=self.kwargs["contrat"])


class Calendrier_HebdomadaireListView(TUTMixin,AdminListView):
    model = Calendrier_Hebdomadaire
    menu="contrat"
    nav_active="calendrier_hebdomadaire"
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        contrat=Contrat.objects.get(pk=self.kwargs["contrat"])
        groupe_tp=contrat.affectation.groupe_set.filter(type="TP")
        return queryset.filter(calendrier__promotion=contrat.affectation.promotion,calendrier__groupe=groupe_tp)

class FormationListView(TUTMixin,AdminListView):
    model = UE
    menu="contrat"
    nav_active="formation"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        contrat=Contrat.objects.get(pk=self.kwargs["contrat"])
        return queryset.filter(formation=contrat.affectation.promotion.formation)


class Fiche_LiaisonDetailView(TUTMixin,AdminDetailView):
    model = Fiche_Liaison
    menu="contrat"
    nav_active="fiche"

    def get_object(self, queryset=None):
        contrat=Contrat.objects.get(pk=self.kwargs["contrat"])
        return contrat.fiche_liaison


