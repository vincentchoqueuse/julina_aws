
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from generic.views import *

# Formation

class FormationView(RafMixin,AdminDetailView):
    model = Formation
    is_markdown=True
    menu="formation"
    pk_url_kwarg = "formation"
    template_name="admin_raf/formation_index.html"

# reseau

class ReseauUpdateView(RafMixin,AjaxableUpdateMixin):
    model=Formation
    fields =  ["linkedin","facebook"]
    pk_url_kwarg = "formation"


# Parcours

class ParcoursView(RafMixin,AdminListView):
    model = Parcours
    menu="formation"
    title="Liste des parcours"
    nav_active="maquette"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(formation=self.kwargs["formation"])

class ParcoursCreateView(RafMixin,AjaxableCreateMixin):
    model=Parcours
    fields=["nom","nom_short","ues"]
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['ues'].queryset = UE.objects.filter(formation=self.kwargs["formation"])
        return form
    
    def form_valid(self, form):
        form.instance.formation = get_object_or_404(Formation,pk=self.kwargs["formation"])
        return super().form_valid(form)

class ParcoursUpdateView(RafMixin,AjaxableUpdateMixin):
    model=Parcours
    fields=["nom","nom_short","ues"]
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["ues"].queryset = UE.objects.filter(formation=self.object.formation)
        return form

class ParcoursDeleteView(RafMixin,AjaxableDeleteMixin):
    model=Parcours

# UE


class UECreateView(RafMixin,AjaxableCreateMixin):
    model=UE
    menu="formation"
    fields=["numero","intitule","nb_heures","nb_ects","coefficient"]
    
    def form_valid(self, form):
        form.instance.formation = get_object_or_404(Formation, pk=self.kwargs["formation"])
        return super().form_valid(form)

class UEUpdateView(RafMixin,AjaxableUpdateMixin):
    model=UE
    fields=["numero","intitule","nb_heures","nb_ects","coefficient"]

class UEDeleteView(RafMixin,AjaxableDeleteMixin):
    model=UE

# Module

class ModuleView(RafMixin,AdminListView):
    model = UE
    can_delete=True
    menu="formation"
    list_template="formations/ue_list.html"
    title="Liste des modules"
    nav_active="maquette"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(formation=self.kwargs["formation"])


class ModuleCreateView(RafMixin,AjaxableCreateMixin):
    model=Module
    fields=["ue","code_apogee","code_scodoc","obligatoire","intitule","nb_heures_cours","nb_heures_td","nb_heures_tp","nb_ects","coefficient"]
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['ue'].queryset = form.fields['ue'].queryset.filter(formation=self.kwargs["formation"])
        return form
    
    def form_valid(self, form):
        form.instance.formation = get_object_or_404(Formation, pk=self.kwargs["formation"])
        return super().form_valid(form)

class ModuleUpdateView(RafMixin,AjaxableUpdateMixin):
    model=Module
    fields=["ue","code_apogee","code_scodoc","obligatoire","intitule","nb_heures_cours","nb_heures_td","nb_heures_tp","nb_ects","coefficient"]

class ModuleDeleteView(RafMixin,AjaxableDeleteMixin):
    model=Module

# Consigne

class ConsigneView(RafMixin,AdminDetailView):
    model = Formation
    is_markdown=True
    pk_url_kwarg = "formation"
    menu="formation"
    template_name="admin_raf/formation_consigne.html"
    nav_active="consigne"

class Consigne_Projet_UpdateView(RafMixin,AjaxableUpdateMixin):
    model=Formation
    fields=["consigne_projet","grille_projet"]
    pk_url_kwarg = "formation"

class Consigne_Contrat_UpdateView(RafMixin,AjaxableUpdateMixin):
    model=Formation
    fields=["consigne_contrat","grille_contrat"]
    pk_url_kwarg = "formation"

class Consigne_Feuille_UpdateView(RafMixin,AjaxableUpdateMixin):
    model=Formation
    fields=["consigne_feuille_emargement"]
    pk_url_kwarg = "formation"

# Promotion
class PromotionCreateView(RafMixin,AjaxableCreateMixin):
    
    model=Promotion
    fields=["annee","rentree","active"]
    
    def form_valid(self, form):
        form.instance.formation = get_object_or_404(Formation,pk=self.kwargs["formation"])
        form.instance.responsable=form.instance.formation.responsable
        return super().form_valid(form)

class PromotionUpdateView(RafMixin,AjaxableUpdateMixin):
    
    model=Promotion
    fields=["annee","rentree","active"]

class PromotionDeleteView(RafMixin,AjaxableDeleteMixin):
    
    model=Promotion



