
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from entreprises.models import Tuteur_Entreprise, Contrat, Rapport_Tuteur_Entreprise
from generic.views import *
from django.contrib.auth.mixins import UserPassesTestMixin



############################################


class TUTMixin(UserPassesTestMixin):
    
    login_url = "/login/"
    url_prefix="admin_tut"
    
    def test_func(self):
        if hasattr(self.request.user,'tuteur_entreprise'):
            output=True
        else:
            output=False
        return output
