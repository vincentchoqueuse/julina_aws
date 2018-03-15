
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from formations.models import Departement, Formation, UE, Module, Parcours, Enseignant, Administratif
from promotions.models import Promotion, Groupe, Etudiant, Affectation_Etudiant, Affectation_Enseignant, Calendrier, Absence
from generic.views import *
from django.contrib.auth.mixins import UserPassesTestMixin



############################################

class ADMMixin(UserPassesTestMixin):
    
    login_url = "/login/"
    url_prefix="admin_adm"
    
    def test_func(self):
        if hasattr(self.request.user,'administratif'):
            output=True
        else:
            output=False
        return output


class AdministratifDetailView(ADMMixin,AdminDetailView):
    model = Administratif
    template_name="admin_adm/index.html"
    
    def get_object(self, queryset=None):
        return self.request.user.administratif

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["promotion_list"]=Promotion.objects.filter(formation__departement=self.request.user.administratif.departement_set.all(),active=True)
        return context

class AbsenceListView(ADMMixin,AdminListView):
    model = Absence
    template_name="admin_adm/absence_list.html"
    
    def get_queryset(self):
        queryset=super().get_queryset()
        queryset.filter(affectation_etudiant__promotion__formation__departement__in=self.request.user.administratif.departement_set.all())
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sidebar_menu"]="database"
        context["is_adm"]=True
        return context

class EnseignantListView(ADMMixin,AdminListView):
    model = Enseignant
    template_name="admin_adm/enseignant_list.html"
    
    def get_queryset(self):
        queryset=super().get_queryset()
        queryset.filter(departement_enseignant__in=self.request.user.administratif.departement_set.all())
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sidebar_menu"]="database"
        return context

class EtudiantListView(ADMMixin,AdminListView):
    model = Etudiant
    template_name="admin_adm/etudiant_list.html"
    
    def get_queryset(self):
        queryset=super().get_queryset()
        queryset.filter(promotion__formation__departement__in=self.request.user.administratif.departement_set.all())
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sidebar_menu"]="database"
        return context

class PromotionDetailView(ADMMixin,AdminDetailView):
    model = Promotion
    template_name="admin_adm/promotion_detail.html"


## AJAX
class AdministratifUpdateView(ADMMixin,AjaxableUpdateMixin):
    model=Administratif
    fields =  ["nom","prenom","email","telephone","role","commentaires"]
    
    def get_object(self, queryset=None):
        return self.request.user.administratif

    def form_valid(self, form):
        self.object = form.save()
        html=render_to_string("admin_adm/administratif_detail.html",{"object":self.object,},request=self.request,)
        return JsonResponse({"administratif_detail":html})


class EnseignantUpdateView(ADMMixin,AjaxableUpdateMixin):
    model=Enseignant
    fields =  ["nom","prenom","email","telephone"]
    
    def form_valid(self, form):
        self.object = form.save()
        object_list=Enseignant.objects.filter(departement_enseignant__in=self.request.user.administratif.departement_set.all())
        html=render_to_string("formations/enseignant_list.html",{"object_list":object_list,},request=self.request,)
        return JsonResponse({"enseignant_table":html})

class AbsenceUpdateView(ADMMixin,AjaxableUpdateMixin):
    model=Absence
    fields =  ["debut","fin","commentaire_adm","statut","justification"]
    
    def form_valid(self, form):
        self.object = form.save()
        object_list=Absence.objects.filter(affectation_etudiant__promotion__formation__departement__in=self.request.user.administratif.departement_set.all())
        html=render_to_string("promotions/absence_list.html",{"object_list":object_list,"is_adm":True},request=self.request,)
        return JsonResponse({"absence_table":html})




