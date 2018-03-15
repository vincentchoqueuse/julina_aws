from formations.models import Formation,Parcours
from promotions.models import Groupe, Promotion
from django import forms
from .models import *


class FilterForm(forms.Form):
    actif=forms.BooleanField(required=False,help_text="resultat actif uniquement",initial=True)

class EnseignantFilterForm(forms.Form):
    STATUT_CHOICES = ( ('I', 'Indifferent'),
                      ('P', 'Permanent'),
                      ('V', 'Vacataire'),
                      )
    nom=forms.CharField(required=False)
    statut=forms.ChoiceField(choices=STATUT_CHOICES, required=False, label='Statut',widget=forms.Select(attrs={'class' :"custom-select"}))
    promotion=forms.ModelMultipleChoiceField(required=False,queryset=Promotion.objects.all())


class FormationFilterForm(forms.Form):
    mention=forms.CharField(required=False)
    departement=forms.ModelChoiceField(required=False,queryset=Departement.objects.all(),empty_label="departement",widget=forms.Select(attrs={'class' :"custom-select"}))
