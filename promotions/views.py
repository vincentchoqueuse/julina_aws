from django.shortcuts import render

from .models import *
from generic.views import *
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from projets.models import *
from formations.models import *
from django import forms

## Etudiant


# Standard



# Etudiant




class EtudiantDetailView(AjaxableDetailMixin):
    model=Etudiant
    template_name="promotions/etudiant_detail.html"





# AJAX

class PromotionDetailView(AjaxableDetailMixin):
    model=Promotion
    template_name="promotions/promotion_detail.html"

class GroupeDetailView(AjaxableDetailMixin):
    model=Groupe
    template_name="promotions/groupe_detail.html"

class Affectation_EtudiantDetailView(AjaxableDetailMixin):
    model=Affectation_Etudiant
    template_name="promotions/affectation_etudiant_detail.html"


class CalendrierDetailView(AjaxableDetailMixin):
    model=Calendrier
    template_name="promotions/calendrier_detail.html"


class BulletinDetailView(AjaxableDetailMixin):
    model=Bulletin
    template_name="promotions/bulletin_detail.html"

class AbsenceDetailView(AjaxableDetailMixin):
    model=Absence
    template_name="promotions/absence_detail.html"

