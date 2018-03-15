from .models import *
from generic.views import *
from entreprises.models import *

class Projet_TuteureDetailView(ETUMixin,AdminDetailView):
    model=Projet_Tuteure
    pk_url_kwarg = "projet_tuteure"
    template_name="admin_etu/projet_tuteure_detail.html"
    nav_active="detail"
    menu="projet_tuteure"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["suivi_projet_list"]=self.object.suivi_projet_set.all()
        context["affectation_etudiant_list"]=self.object.affectation.all()
        return context

class Suivi_ProjetCreateView(ETUMixin,AjaxableCreateMixin):
    model=Suivi_Projet
    fields=["nombre_heures","travail_effectue","difficultes","suite"]
    
    def form_valid(self, form):
        form.instance.projet = get_object_or_404(Projet_Tuteure,pk=self.kwargs["projet_tuteure"])
        return super().form_valid(form)

class Suivi_ProjetUpdateView(ETUMixin,AjaxableUpdateMixin):
    model=Suivi_Projet
    fields=["nombre_heures","travail_effectue","difficultes","suite"]

class Suivi_ProjetDeleteView(ETUMixin,AjaxableDeleteMixin):
    model=Suivi_Projet


class DescriptionDetailView(ETUMixin,AdminDetailView):
    model=Projet_Tuteure
    pk_url_kwarg = "projet_tuteure"
    title="Description Projet Tuteuré"
    nav_active="description"
    menu="projet_tuteure"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["suivi_projet_list"]=self.object.suivi_projet_set.all()
        context["affectation_etudiant_list"]=self.object.affectation.all()
        return context

class ConsigneDetailView(ETUMixin,AdminDetailView):
    model=Projet_Tuteure
    pk_url_kwarg = "projet_tuteure"
    detail_template="formations/consigne_projet_detail.html"
    title="Consigne"
    nav_active="consigne"
    menu="projet_tuteure"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"]=self.object.promotion.formation
        return context
