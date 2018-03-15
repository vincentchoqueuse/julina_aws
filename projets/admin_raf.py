from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from promotions.models import *
from .models import *
from generic.views import *



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

