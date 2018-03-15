from .models import *
from generic.views import *
from .forms import *
import csv
from django.http import HttpResponse
from django.template import loader, Context

# Standard

class EntrepriseExportView(AjaxableFormMixin):
    form_class = EntrepriseFilterForm2
    
    def form_valid(self, form):
        
        entreprises=Entreprise.objects.filter(contrat__affectation__promotion__formation__in=form.cleaned_data["formation"]).distinct()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
        t = loader.get_template('entreprises/entreprise_list.csv')
        response.write(t.render({'object_list': entreprises.all()}))
        return response


class EntrepriseListView(admin_Mixin,AdminListView):
    model = Entreprise
    paginate_by = 20
    can_export=True
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = EntrepriseFilterForm(self.request.GET)
        if self.form.is_valid():
            
            if self.form.cleaned_data["nom"]:
                queryset=queryset.filter(nom__contains=self.form.cleaned_data["nom"])
            if self.form.cleaned_data["promotion"]:
                queryset=queryset.filter(contrat__affectation__promotion=self.form.cleaned_data["promotion"])
            if self.form.cleaned_data["formation"]:
                queryset=queryset.filter(contrat__affectation__promotion__formation=self.form.cleaned_data["formation"])
                self.form.fields["promotion"].queryset=Promotion.objects.filter(formation=self.form.cleaned_data["formation"])
        
        return queryset.distinct()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"]=self.form
        return context

class CarteListView(admin_Mixin,AdminListView):
    model = Entreprise
    template_name="entreprises/entreprise_carte_list.html"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = EntrepriseFilterForm(self.request.GET)
        if self.form.is_valid():
            
            if self.form.cleaned_data["nom"]:
                queryset=queryset.filter(nom__contains=self.form.cleaned_data["nom"])
            if self.form.cleaned_data["promotion"]:
                queryset=queryset.filter(contrat__affectation__promotion=self.form.cleaned_data["promotion"])
            if self.form.cleaned_data["formation"]:
                queryset=queryset.filter(contrat__affectation__promotion__formation=self.form.cleaned_data["formation"])
                self.form.fields["promotion"].queryset=Promotion.objects.filter(formation=self.form.cleaned_data["formation"])
        
        return queryset.distinct()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"]=self.form
        return context

class EntrepriseCreateView(AjaxableCreateMixin):
    model=Entreprise
    fields=["siret","nom","statut","naf","activite","adresse_rue","adresse_zip","adresse_ville","gps_lat","gps_long",]

class EntrepriseUpdateView(AjaxableUpdateMixin):
    model=Entreprise
    fields=["nom","statut","naf","activite","adresse_rue","adresse_zip","adresse_ville","gps_lat","gps_long",]

class EntrepriseDeleteView(AjaxableDeleteMixin):
    model=Entreprise

# Tuteur

class Tuteur_EntrepriseListView(admin_Mixin,AdminListView):
    model = Tuteur_Entreprise
    paginate_by = 20
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = TuteurFilterForm(self.request.GET)
        if self.form.is_valid():
            if self.form.cleaned_data["nom"]:
                queryset=queryset.filter(nom__contains=self.form.cleaned_data["nom"])
            if self.form.cleaned_data["entreprise"]:
                queryset=queryset.filter(contrat__entreprise=self.form.cleaned_data["entreprise"])

        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"]=self.form
        return context

class Tuteur_EntrepriseCreateView(AjaxableCreateMixin):
    model=Tuteur_Entreprise
    fields=["nom","prenom","email","poste","telephonemobile"]

class Tuteur_EntrepriseUpdateView(AjaxableUpdateMixin):
    model=Tuteur_Entreprise
    fields=["email","poste","telephonemobile"]

class Tuteur_EntrepriseDeleteView(AjaxableDeleteMixin):
    model=Tuteur_Entreprise


# Rapport Tuteur Entreprise

class Rapport_Tuteur_EntrepriseListView(admin_Mixin,AdminListView):
    model = Rapport_Tuteur_Entreprise
    paginate_by = 20
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = TuteurFilterForm(self.request.GET)
        if self.form.is_valid():
            if self.form.cleaned_data["nom"]:
                queryset=queryset.filter(nom__contains=self.form.cleaned_data["nom"])
            if self.form.cleaned_data["entreprise"]:
                queryset=queryset.filter(contrat__entreprise=self.form.cleaned_data["entreprise"])
        
        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"]=self.form
        return context

class Rapport_Tuteur_EntrepriseCreateView(AjaxableCreateMixin):
    model=Rapport_Tuteur_Entreprise
    fields=["contrat","deadline","actif"]

class Rapport_Tuteur_EntrepriseUpdateView(AjaxableUpdateMixin):
    model=Rapport_Tuteur_Entreprise
    fields=["contrat","deadline","actif"]

class Rapport_Tuteur_EntrepriseDeleteView(AjaxableDeleteMixin):
    model=Rapport_Tuteur_Entreprise

# Rapport Tuteur Formation

class Rapport_Tuteur_FormationListView(admin_Mixin,AdminListView):
    model = Rapport_Tuteur_Formation
    paginate_by = 20
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = TuteurFilterForm(self.request.GET)
        if self.form.is_valid():
            if self.form.cleaned_data["nom"]:
                queryset=queryset.filter(nom__contains=self.form.cleaned_data["nom"])
            if self.form.cleaned_data["entreprise"]:
                queryset=queryset.filter(contrat__entreprise=self.form.cleaned_data["entreprise"])

        return queryset.distinct()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"]=self.form
        return context

class Rapport_Tuteur_FormationCreateView(AjaxableCreateMixin):
    model=Rapport_Tuteur_Formation
    fields=["contrat","commentaires"]

class Rapport_Tuteur_FormationUpdateView(AjaxableUpdateMixin):
    model=Rapport_Tuteur_Formation
    fields=["activite","visite","commentaires"]

class Rapport_Tuteur_FormationDeleteView(AjaxableDeleteMixin):
    model=Rapport_Tuteur_Formation
