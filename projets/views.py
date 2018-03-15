from django.shortcuts import render
from generic.views import *
from .models import Projet_Tuteure, Suivi_Projet
from promotions.models import *
from formations.models import *

# Create your views here.


class Projet_TuteureDetailView(AjaxableDetailMixin):
    model=Projet_Tuteure
    template_name="projets/projet_tuteure_detail.html"

class Suivi_ProjetDetailView(AjaxableDetailMixin):
    model=Suivi_Projet
    template_name="projets/suivi_projet_detail.html"

