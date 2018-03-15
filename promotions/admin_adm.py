from .models import *
from formations.models import *
from generic.views import *
from projets.views import *
from entreprises.models import *
from .forms import *

##### MENU PROMOTION

class PromotionDetailView(ADMMixin,AdminDetailView):
    model = Promotion
    pk_url_kwarg = "promotion"
    menu = "promotion"
    template_name="admin_adm/promotion_detail.html"
    nav_active="detail"


class MaquetteListView(ADMMixin,AdminListView):
    model = UE
    menu = "promotion"
    title="Liste des Modules"
    nav_active="formation"
    can_update=False
    can_delete=False
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(formation__promotion=self.kwargs["promotion"])


class Affectation_EtudiantListView(ADMMixin,AdminListView):
    model = Affectation_Etudiant
    menu = "promotion"
    can_update=False
    can_delete=False
    can_filter=True
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(promotion=self.kwargs["promotion"])
        self.form = Affectation_EtudiantFilterForm(self.kwargs["promotion"],self.request.GET)
        if self.form.is_valid():
            if self.form.cleaned_data["groupe"]:
                queryset=queryset.filter(groupe=self.form.cleaned_data["groupe"])

        return queryset.distinct()

class Affectation_EnseignantListView(ADMMixin,AdminListView):
    model = Affectation_Enseignant
    menu = "promotion"
    can_update=False
    can_delete=False
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(groupe__promotion=self.kwargs["promotion"])


class EmargementListView(ADMMixin,AdminListView):
    
    model = Calendrier_Hebdomadaire
    can_filter=True
    menu = "promotion"
    nav_active="emargement"
    title="Responsables de la feuille d'emargement"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(calendrier__promotion=self.kwargs["promotion"])
        self.form = Calendrier_HebdomadaireFilterForm(self.kwargs["promotion"],self.request.GET)
        if self.form.is_valid():
            if self.form.cleaned_data["groupe"]:
                queryset=queryset.filter(calendrier__groupe=self.form.cleaned_data["groupe"])

        return queryset.distinct()

# Contrat

class ContratListView(ADMMixin,AdminListView):
    model = Contrat
    menu = "promotion"
    can_update=False
    can_delete=False
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(affectation__promotion=self.kwargs["promotion"])

# Projet

class Projet_TuteureListView(ADMMixin,AdminListView):
    model = Projet_Tuteure
    menu = "promotion"
    can_update=False
    can_delete=False
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(affectation__promotion=self.kwargs["promotion"]).distinct()


# Absence

class AbsenceListView(ADMMixin,AdminListView):
    
    model = Absence
    menu = "promotion"
    can_create="True"
    can_update="True"
    can_delete="Delete"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(affectation_etudiant__promotion=self.kwargs["promotion"])

class AbsenceCreateView(ADMMixin,AjaxableCreateMixin):
    model=Absence
    fields=["affectation_etudiant","debut","fin","commentaire_adm","justification","statut"]
    
    def form_valid(self, form):
        self.object = form.save()
        self.object.enseignants.add(self.request.user.enseignant)
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["affectation_etudiant"].queryset = form.fields["affectation_etudiant"].queryset.filter(promotion__pk=self.kwargs["promotion"])
        return form



class AbsenceUpdateView(ADMMixin,AjaxableUpdateMixin):
    model=Absence
    fields=["debut","fin","commentaire_adm","justification","statut"]

class AbsenceDeleteView(ENSMixin,AjaxableDeleteMixin):
    model=Absence
