from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from formations.models import *
from promotions.models import *
from entreprises.models import *
from projets.models import *
from generic.views import *
from .forms import *

#Promotion

class PromotionDetailView(RafMixin,AdminDetailView):
    model = Promotion
    is_markdown=True
    menu="promotion"
    template_name="admin_raf/promotion_index.html"
    pk_url_kwarg = "promotion"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["promotion"]=self.object
        return context

#BUlletin
class PromotionBulletinImportView(RafMixin,AjaxableFormMixin):
    form_class = BulletinImportForm
    
    def form_valid(self, form):
        form.fields["promotion"]=get_object_or_404(Promotion,pk=self.kwargs["promotion"])
        form.process_form(self.request)
        return super().form_valid(form)


# Groupe

class GroupeCreateView(RafMixin,AjaxableCreateMixin):
    model=Groupe
    fields=["nom","type"]
    
    def form_valid(self, form):
        form.instance.promotion= get_object_or_404(Promotion,pk=self.kwargs["promotion"])
        return super().form_valid(form)

class GroupeUpdateView(RafMixin,AjaxableUpdateMixin):
    model=Groupe
    fields=["nom","type"]

class GroupeDeleteView(RafMixin,AjaxableDeleteMixin):
    model=Groupe
    url_prefix="admin_raf"

# Affectation Enseignant

class Affectation_EnseignantView(RafMixin,AdminListView):
    model=Affectation_Enseignant
    menu="promotion"
    title="Affectation Enseignant"
    nav_active="affectation_enseignant"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(groupe__promotion=self.kwargs["promotion"])

class Affectation_EnseignantCreateView(RafMixin,AjaxableCreateMixin):
    model=Affectation_Enseignant
    fields=["enseignant","module","groupe","nb_heures"]
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        promotion=get_object_or_404(Promotion,pk=self.kwargs["promotion"])
        form.fields["enseignant"].queryset = Enseignant.objects.filter(formation=promotion.formation)
        form.fields["groupe"].queryset = Groupe.objects.filter(promotion=promotion)
        form.fields["module"].queryset = Module.objects.filter(ue__formation=promotion.formation)
        return form


class Affectation_EnseignantUpdateView(RafMixin,AjaxableUpdateMixin):
    model=Affectation_Enseignant
    fields=["enseignant","module","groupe","nb_heures"]
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["enseignant"].queryset = Enseignant.objects.filter(formation=self.object.groupe.promotion.formation)
        form.fields["groupe"].queryset = Groupe.objects.filter(promotion=self.object.groupe.promotion)
        form.fields["module"].queryset = Module.objects.filter(ue__formation=self.object.groupe.promotion.formation)
        return form

class Affectation_EnseignantDeleteView(RafMixin,AjaxableDeleteMixin):
    model=Affectation_Enseignant


# Affectation Etudiant

class Affectation_EtudiantView(RafMixin,AdminListView):
    model=Affectation_Etudiant
    menu="promotion"
    title="Affectation Etudiant"
    can_create=False
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(promotion=self.kwargs["promotion"])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["groupes"]=Groupe.objects.filter(promotion=self.kwargs["promotion"])
        return context

class Affectation_EtudiantUpdateView(RafMixin,AjaxableUpdateMixin):
    form_class = AffectationEtudiantForm
    model=Affectation_Etudiant
    
    def get_initial(self):
        initial=super().get_initial()
        initial["groupe_cours"]=Groupe.objects.filter(promotion=self.object.promotion,type="C",affectations=self.object).first()
        initial["groupe_td"]=Groupe.objects.filter(promotion=self.object.promotion,type="TD",affectations=self.object).first()
        initial["groupe_tp"]=Groupe.objects.filter(promotion=self.object.promotion,type="TP",affectations=self.object).first()
        return initial
    
    def get_form(self, form_class=None):
        form=super().get_form(form_class)
        
        form.fields["parcours"].queryset = Parcours.objects.filter(formation=self.object.promotion.formation)
        form.fields["groupe_cours"].queryset = Groupe.objects.filter(promotion=self.object.promotion,type="C")
        form.fields["groupe_td"].queryset = Groupe.objects.filter(promotion=self.object.promotion,type="TD")
        form.fields["groupe_tp"].queryset = Groupe.objects.filter(promotion=self.object.promotion,type="TP")
        return form
    
    def form_valid(self, form):
        #on supprime les anciennes affectations
        groupes=Groupe.objects.filter(affectations=self.object).all()
        for groupe in groupes:
            groupe.affectations.remove(self.object)
        
        form.cleaned_data["groupe_cours"].affectations.add(self.object)
        form.cleaned_data["groupe_td"].affectations.add(self.object)
        form.cleaned_data["groupe_tp"].affectations.add(self.object)
        return super().form_valid(form)

class Affectation_EtudiantDeleteView(RafMixin,AjaxableDeleteMixin):
    model=Affectation_Etudiant


# Calendrier

class CalendrierView(RafMixin,AdminListView):
    model=Calendrier_Hebdomadaire
    menu="promotion"
    title="Calendrier"
    nav_active="calendrier_hebdomadaire"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(calendrier__groupe__promotion=self.kwargs["promotion"])

class CalendrierCreateView(RafMixin,AjaxableCreateMixin):
    model=Calendrier
    fields=["groupe","ics","commentaire"]
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["groupe"].queryset = Groupe.objects.filter(promotion__pk=self.kwargs["promotion"],type="TP")
        return form
    
    def form_valid(self, form):
        form.instance.promotion = get_object_or_404(Promotion,pk=self.kwargs["promotion"])
        return super().form_valid(form)

class CalendrierUpdateView(RafMixin,AjaxableUpdateMixin):
    model=Calendrier
    fields=["groupe","ics","commentaire"]
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["groupe"].queryset = Groupe.objects.filter(promotion=self.object.promotion,type="TP")
        return form

class CalendrierDeleteView(RafMixin,AjaxableDeleteMixin):
    model=Calendrier

class Calendrier_HebdomadaireCreateView(RafMixin,AjaxableCreateMixin):
    model=Calendrier_Hebdomadaire
    fields=["calendrier","num_semaine","annee","commentaire"]
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["calendrier"].queryset = Calendrier.objects.filter(promotion__pk=self.kwargs["promotion"])
        return form

class Calendrier_HebdomadaireUpdateView(RafMixin,AjaxableUpdateMixin):
    model=Calendrier_Hebdomadaire
    fields=["num_semaine","annee","responsable","commentaire"]
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["responsable"].queryset=self.object.calendrier.groupe.affectations
        return form

class Calendrier_HebdomadaireDeleteView(RafMixin,AjaxableDeleteMixin):
    model=Calendrier_Hebdomadaire

# Contrat

class ContratView(RafMixin,AdminListView):
    template_name="admin_raf/promotion_contrat.html"
    menu="promotion"
    model=Contrat
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(affectation__promotion=self.kwargs["promotion"])

# Projet

class ProjetListView(RafMixin,AdminListView):
    model=Projet_Tuteure
    menu="promotion"
    title="Projet Tuteure"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(promotion=self.kwargs["promotion"])

class Projet_TuteureCreateView(RafMixin,AjaxableCreateMixin):
    model=Projet_Tuteure
    fields=["enseignant","affectation","intitule","salle","problematique","methodologie","remarque","actif"]
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["affectation"].queryset = Affectation_Etudiant.objects.filter(promotion__pk=self.kwargs["promotion"])
        return form
    
    def form_valid(self, form):
        form.instance.promotion = get_object_or_404(Promotion,pk=self.kwargs["promotion"])
        return super().form_valid(form)

class Projet_TuteureUpdateView(RafMixin,AjaxableUpdateMixin):
    model=Projet_Tuteure
    fields=["enseignant","affectation","intitule","salle","problematique","methodologie","remarque","actif"]
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["affectation"].queryset = Affectation_Etudiant.objects.filter(promotion=self.object.promotion)
        return form

class Projet_TuteureDeleteView(RafMixin,AjaxableDeleteMixin):
    model=Projet_Tuteure
    url_prefix="admin_raf"


# Projet



# Absence

class AbsenceView(RafMixin,AdminListView):
    model=Absence
    menu="promotion"
    title="Absence"
    nav_active="absence"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(affectation_etudiant__promotion=self.kwargs["promotion"])


class AbsenceCreateView(RafMixin,AjaxableCreateMixin):
    model=Absence
    fields=["affectation_etudiant","debut","fin","commentaire_raf","statut","enseignants","justification"]
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["affectation_etudiant"].queryset = form.fields["affectation_etudiant"].queryset.filter(promotion__pk=self.kwargs["promotion"])
        form.fields["enseignants"].queryset = form.fields["enseignants"].queryset.filter(affectation_enseignant_set__groupe__promotion__pk=self.kwargs["promotion"]).distinct()
        return form

class AbsenceUpdateView(RafMixin,AjaxableUpdateMixin):
    model=Absence
    fields=["debut","fin","commentaire_raf","statut","enseignants","justification"]
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["enseignants"].queryset = form.fields["enseignants"].queryset.filter(affectation_enseignant_set__groupe__promotion__pk=self.object.affectation_etudiant.promotion.pk).distinct()
        return form

class AbsenceDeleteView(RafMixin,AjaxableDeleteMixin):
    model=Absence


class ContratCreateView(RafMixin,AjaxableCreateMixin):
    model=Contrat
    fields=["type","entreprise","affectation","intitule","tuteur_entreprise","tuteur_formation","opca","remarques","cqpm"]
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["affectation"].queryset = Affectation_Etudiant.objects.filter(promotion__pk=self.kwargs["promotion"])
        return form

class ContratUpdateView(RafMixin,AjaxableUpdateMixin):
    model=Contrat
    fields=["type","entreprise","affectation","intitule","tuteur_entreprise","tuteur_formation","opca","remarques","cqpm"]
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["affectation"].queryset = Affectation_Etudiant.objects.filter(promotion=self.object.affectation.promotion)
        return form

class ContratDeleteView(RafMixin,AjaxableDeleteMixin):
    model=Contrat

class ContratImportView(RafMixin,AjaxableFormMixin):
    form_class = ContratImportForm
    template_name="modal_form_import.html"
    
    def get_object_list(self):
        return Contrat.objects.filter(affectation__promotion__pk=self.kwargs["promotion"])
    
    def process_form(self,form):
        form.promotion= get_object_or_404(Promotion,pk=self.kwargs["promotion"])
        form.process_form(self.request)
        return form


# Page Rapport Tuteur Entreprise


class Rapport_Tuteur_EntrepriseView(RafMixin,AdminListView):
    model=Rapport_Tuteur_Entreprise
    menu = "promotion"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(contrat__affectation__promotion=self.kwargs["promotion"])

class Rapport_Tuteur_EntrepriseFormView(RafMixin,AjaxableFormMixin):
    form_class = Rapport_Tuteur_EntrepriseForm
    
    def process_form(self,form):
        nom=form.cleaned_data["nom"]
        deadline=form.cleaned_data["deadline"]
        contrat_list=form.cleaned_data["contrat_list"]
        
        for contrat in contrat_list:
            p = Rapport_Tuteur_Entreprise.objects.create(nom=nom,deadline=deadline,contrat=contrat)
        return form
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['contrat_list'].queryset = form.fields['contrat_list'].queryset.filter(affectation__promotion__pk=self.kwargs["promotion"])
        return form

class Rapport_Tuteur_EntrepriseUpdateView(RafMixin,AjaxableUpdateMixin):
    model=Rapport_Tuteur_Entreprise
    fields=["nom","deadline","actif"]

class Rapport_Tuteur_EntrepriseDeleteView(RafMixin,AjaxableDeleteMixin):
    model=Rapport_Tuteur_Entreprise



