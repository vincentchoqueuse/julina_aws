from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from .models import *
from generic.views import *


##### MENU PROJET


class Projet_TuteureDetailView(ENSMixin,AdminDetailView):
    model = Projet_Tuteure
    template_name="admin_ens/projet_tuteure_detail.html"
    pk_url_kwarg = "projet_tuteure"
    menu="projet_tuteure"
    nav_active="detail"

class Projet_Tuteure2DetailView(ENSMixin,AdminDetailView):
    model = Projet_Tuteure
    pk_url_kwarg = "projet_tuteure"
    menu="projet_tuteure"
    nav_active="projet"

class ConsigneDetailView(ENSMixin,AdminDetailView):
    can_update=False
    model = Projet_Tuteure
    detail_template="formations/consigne_projet_detail.html"
    pk_url_kwarg = "projet_tuteure"
    menu="projet_tuteure"
    nav_active="consigne"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"]=self.object.promotion.formation
        return context

class Projet_TuteureUpdateView(ENSMixin,AjaxableUpdateMixin):
    model=Projet_Tuteure
    fields=["intitule","salle","contexte","problematique","methodologie","remarque"]
    pk_url_kwarg = "projet_tuteure"


class Suivi_ProjetUpdateView(ENSMixin,AjaxableUpdateMixin):
    model=Suivi_Projet
    fields=["remarques"]
    pk_url_kwarg = "projet_tuteure"









