
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from formations.models import Departement, Formation, UE, Module, Parcours, Enseignant
from promotions.models import Promotion, Groupe, Etudiant, Affectation_Etudiant, Affectation_Enseignant, Calendrier
from generic.views import *



############################################


class DepartementDetailView(AdminDetailView):
    model = Departement
    template_name="admin_dep/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["promotion_list"]=Promotion.objects.filter(formation__departement=self.object,active=True)
        
        return context

class PromotionDetailView(AdminDetailView):
    model = Promotion
    template_name="admin_dep/promotion_detail.html"
    

