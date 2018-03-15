from django import forms
from .models import *
from formations.models import *
from promotions.models import *

class EntrepriseFilterForm(forms.Form):
    nom=forms.CharField(required=False)
    formation = forms.ModelChoiceField(required=False,queryset=Formation.objects.all(),empty_label="Formation",widget=forms.Select(attrs={'class' :"custom-select"}))
    promotion=forms.ModelChoiceField(required=False,queryset=Promotion.objects.all(),empty_label="Promotion",widget=forms.Select(attrs={'class' :"custom-select"}))

class EntrepriseFilterForm2(forms.Form):
    formation = forms.ModelMultipleChoiceField(required=False,queryset=Formation.objects.all())

class TuteurFilterForm(forms.Form):
    nom=forms.CharField(required=False)
    entreprise=forms.ModelChoiceField(required=False,queryset=Entreprise.objects.all(),empty_label="Entreprise",widget=forms.Select(attrs={'class' :"custom-select"}))



class ContratImportForm(forms.Form):
    file = forms.FileField()
    
    def process_form(self,request):
        
        promotion=self.promotion
        formation=self.promotion.formation
        input_excel = request.FILES["file"]
        workbook = xlrd.open_workbook(file_contents=input_excel.read())
        
        sheet = workbook.sheet_by_index(0)
        nb_rows=sheet.nrows
        
        
        for num_row in range(1,nb_rows):
            
            try:
                etudiant_nom=sheet.cell(num_row,1).value
                etudiant_prenom=sheet.cell(num_row,2).value
                nom_entreprise=sheet.cell(num_row,4).value
                adresse_entreprise=sheet.cell(num_row,5).value
                cp_entreprise=sheet.cell(num_row,6).value
                ville_entreprise=sheet.cell(num_row,7).value
                siret_entreprise=sheet.cell(num_row,8).value
                tel_entreprise=sheet.cell(num_row,9).value
                mail_entreprise=sheet.cell(num_row,10).value
                responsable_administratif_nom=sheet.cell(num_row,11).value
                responsable_administratif_prenom=sheet.cell(num_row,12).value
                opca=sheet.cell(num_row,13).value
                tuteur_entreprise_nom=sheet.cell(num_row,15).value
                tuteur_entreprise_prenom=sheet.cell(num_row,16).value
                tel_tuteur_entreprise=sheet.cell(num_row,17).value
                mail_tuteur_entreprise=sheet.cell(num_row,18).value
                
                affectation=Affectation_Etudiant.objects.get(etudiant__nom=etudiant_nom,etudiant__prenom=etudiant_prenom,promotion=promotion)
                
                entreprise=Entreprise.objects.filter(siret=siret_entreprise)
                if entreprise.exists():
                    entreprise=entreprise[0]
                else:
                    entreprise=Entreprise.objects.create(siret=siret_entreprise,nom=nom_entreprise,adresse_rue=adresse_entreprise,adresse_zip=cp_entreprise,adresse_ville=ville_entreprise)
                    formation.entreprises.add(entreprise)
                
                responsable=Responsable_Administratif.objects.filter(nom=responsable_administratif_nom,prenom=responsable_administratif_prenom)
                if responsable.exists():
                    responsable=responsable[0]
                else:
                    responsable=Responsable_Administratif.objects.create(nom = responsable_administratif_nom,prenom = responsable_administratif_prenom,email=mail_entreprise,telephonemobile=tel_entreprise)
                
                tuteur=Tuteur_Entreprise.objects.filter(nom=tuteur_entreprise_nom,prenom=tuteur_entreprise_prenom)
                if tuteur.exists():
                    tuteur=tuteur[0]
                else:
                    tuteur=Tuteur_Entreprise.objects.create(nom = tuteur_entreprise_nom,prenom = tuteur_entreprise_prenom,email=mail_tuteur_entreprise,telephonemobile=tel_tuteur_entreprise)
                    formation.tuteur_entreprises.add(tuteur)
                
                #creation du contrat
                
                contrat=Contrat.objects.get_or_create(type="CP",affectation=affectation,responsable_administratif=responsable,tuteur_entreprise=tuteur,entreprise=entreprise,opca=opca)
            except:
                print ("Unexpected error:", sys.exc_info()[0])
                raise
    
        return self



class Rapport_Tuteur_EntrepriseForm(forms.ModelForm):
    
    class Meta:
        model = Rapport_Tuteur_Entreprise
        fields=["nom","deadline"]
    
    contrat_list=forms.ModelMultipleChoiceField(queryset=Contrat.objects.all())


