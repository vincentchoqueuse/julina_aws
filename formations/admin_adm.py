from .models import *
from .forms import *
from generic.views import *
from entreprises.models import *

class AdministratifDetailView(ADMMixin,AdminDetailView):
    model = Administratif
    template_name="admin_adm/profil_index.html"
    menu="profil"
    fields = ["nom","prenom","photo","date_naissance","role","email","telephonemobile","telephone","commentaires"]
    
    def get_object(self, queryset=None):
        return self.request.user.administratif

class AdministratifUpdateView(ADMMixin,AjaxableUpdateMixin):
    model=Administratif
    fields =["nom","prenom","photo","role","email","telephonemobile","telephone","commentaires"]
    
    def get_object(self, queryset=None):
        return self.request.user.administratif



