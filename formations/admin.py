from .models import *
from generic.views import *
from .forms import *
from .models import *
from django.http import HttpResponse
from django.template import loader, Context

# Enseignant

class EnseignantExportView(AjaxableFormMixin):
    form_class = EnseignantFilterForm
    
    def form_valid(self, form):
        
        queryset=Enseignant.objects.filter(nom__contains=form.cleaned_data["nom"],groupes__promotion__in=form.cleaned_data["promotion"]).distinct()
        
        if form.cleaned_data["statut"] != 'I':
            queryset=queryset.filter(statut=form.cleaned_data["statut"])

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="enseignants_list.csv"'
        t = loader.get_template('formations/enseignant_list.csv')
        response.write(t.render({'object_list': queryset}))
        return response

class EnseignantListView(admin_Mixin,AdminListView):
    model = Enseignant
    paginate_by = 20
    nav_active="formation"
    can_export=True
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = EnseignantFilterForm(self.request.GET)
        if self.form.is_valid():
            if self.form.cleaned_data["nom"]:
                queryset=queryset.filter(nom__contains=self.form.cleaned_data["nom"])
            if self.form.cleaned_data["statut"]:
                if self.form.cleaned_data["statut"] != 'I':
                    queryset=queryset.filter(statut=self.form.cleaned_data["statut"])
            if self.form.cleaned_data["promotion"]:
                queryset=queryset.filter(groupes__promotion__in=self.form.cleaned_data["promotion"])
        
        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"]=self.form
        return context



class EnseignantCreateView(AjaxableCreateMixin):
    model=Enseignant
    fields=["nom","prenom","statut","employeur","email","telephonemobile","telephone"]

class EnseignantUpdateView(AjaxableUpdateMixin):
    model=Enseignant
    fields=["statut","employeur","email","telephonemobile","telephone"]

class EnseignantDeleteView(AjaxableDeleteMixin):
    model=Enseignant

# Formation

class FormationListView(admin_Mixin,AdminListView):
    model = Formation
    paginate_by = 20
    nav_active="formation"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = FormationFilterForm(self.request.GET)
        if self.form.is_valid():
            if self.form.cleaned_data["mention"]:
                queryset=queryset.filter(mention__contains=self.form.cleaned_data["mention"])
            if self.form.cleaned_data["departement"]:
                queryset=queryset.filter(departement=self.form.cleaned_data["departement"])
        
        return queryset.distinct()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"]=self.form
        return context


class FormationCreateView(AjaxableCreateMixin):
    model=Formation
    fields=["departement","responsable","niveau","domaine","mention","mention_short","active"]

class FormationUpdateView(AjaxableUpdateMixin):
    model=Formation
    fields=["departement","responsable","niveau","domaine","mention","mention_short","active"]

class FormationDeleteView(AjaxableDeleteMixin):
    model=Formation



