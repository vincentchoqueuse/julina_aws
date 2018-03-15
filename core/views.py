from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView, RedirectView
from promotions.models import Affectation_Etudiant, Affectation_Enseignant,Promotion
from formations.models import Enseignant, Formation

class IndexPage(TemplateView):
    
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['affectation_etudiant_list'] = Affectation_Etudiant.objects.filter(promotion__active=True)
        context['formation_list'] = Formation.objects.filter(active=True)
        context['enseignant_list']=Enseignant.objects.all()
        return context


class LoginRedirectView(RedirectView):
    
    def get(self, request, *args, **kwargs):
        
        self.url="/login/"
        
        try:
            enseignant=request.user.enseignant
            self.url="/admin_ens/profil/"
        except:
            pass

        try:
            etudiant=request.user.etudiant
            self.url="/admin_etu/profil/"
        except:
            pass

        try:
            administratif=request.user.administratif
            self.url="/admin_adm/profil/"
        except:
            pass
        
        try:
            tuteur_entreprise=request.user.tuteur_entreprise
            self.url="/admin_tut/profil/"
        except:
            pass
        

        return super().get(request, args, **kwargs)
