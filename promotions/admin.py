from .models import *
from generic.views import *
from .forms import *

class EtudiantListView(admin_Mixin,AdminListView):
    model = Etudiant
    paginate_by = 20
    nav_active="formation"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = EtudiantFilterForm(self.request.GET)
        if self.form.is_valid():
            if self.form.cleaned_data["nom"]:
                queryset=queryset.filter(nom__contains=self.form.cleaned_data["nom"])
            if self.form.cleaned_data["promotion"]:
                queryset=queryset.filter(affectation_set__promotion=self.form.cleaned_data["promotion"])
        
        return queryset.distinct()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"]=self.form
        return context

class EtudiantCreateView(AjaxableCreateMixin):
    model=Etudiant
    fields=["etudid","etat","nom","prenom","sexe","email","email_perso","domicile","villedomicile","codepostaldomicile","telephonemobile","telephone","bac","bac2"]

class EtudiantUpdateView(AjaxableUpdateMixin):
    model=Etudiant
    fields=["email","email_perso","domicile","villedomicile","codepostaldomicile","telephonemobile","telephone","bac","bac2"]

class EtudiantDeleteView(AjaxableDeleteMixin):
    model=Etudiant


# Promotion

class PromotionListView(admin_Mixin,AdminListView):
    model = Promotion
    paginate_by = 20
    nav_active="formation"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = PromotionFilterForm(self.request.GET)
        if self.form.is_valid():
            if self.form.cleaned_data["departement"]:
                queryset=queryset.filter(formation__departement=self.form.cleaned_data["departement"])
            if self.form.cleaned_data["formation"]:
                queryset=queryset.filter(formation=self.form.cleaned_data["formation"])
            if self.form.cleaned_data["active"]:
                queryset=queryset.filter(active=self.form.cleaned_data["active"])
        
        return queryset.distinct()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"]=self.form
        return context

class PromotionCreateView(AjaxableCreateMixin):
    model=Promotion
    fields=["formation","responsable","annee","rentree","active"]

class PromotionUpdateView(AjaxableUpdateMixin):
    model=Promotion
    fields=["formation","responsable","annee","rentree","active"]

class PromotionDeleteView(AjaxableDeleteMixin):
    model=Promotion
