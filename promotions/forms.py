from formations.models import Formation,Parcours, Departement
from promotions.models import Groupe
from django import forms
from .models import *
from entreprises.models import *





# Utilisation de plusieurs formulaire pour filtrer les résultats utilisées dans les LIstview

class Calendrier_HebdomadaireFilterForm(forms.Form):
    groupe=forms.ModelChoiceField(required=False,queryset=Groupe.objects.all(),empty_label="groupe",widget=forms.Select(attrs={'class' :"custom-select"}))


    def __init__(self, promotion_pk, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["groupe"].queryset = Groupe.objects.filter(promotion=promotion_pk,type="TP")

class Affectation_EtudiantFilterForm(forms.Form):
    
    groupe=forms.ModelChoiceField(required=False,queryset=Groupe.objects.all(),empty_label="groupe",widget=forms.Select(attrs={'class' :"custom-select"}))

    def __init__(self, promotion_pk, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["groupe"].queryset = Groupe.objects.filter(promotion=promotion_pk)



class EtudiantFilterForm(forms.Form):
    nom=forms.CharField(required=False)
    promotion=forms.ModelChoiceField(required=False,queryset=Promotion.objects.all(),empty_label="promotion",widget=forms.Select(attrs={'class' :"custom-select"}))


class PromotionFilterForm(forms.Form):
    departement=forms.ModelChoiceField(required=False,queryset=Departement.objects.all(),empty_label="Département",widget=forms.Select(attrs={'class' :"custom-select"}))
    formation = forms.ModelChoiceField(required=False,queryset=Formation.objects.all(),empty_label="Formation",widget=forms.Select(attrs={'class' :"custom-select"}))
    active = forms. BooleanField(required=False)


TRI_CHOICES = (
                  (1, "Etudiant Nom"),
                  (2, "Etudiant Note +"),
                  (3, "Etudiant Note -"),
            )

class PromotionDetailFilterForm(forms.Form):
    tri = forms.ChoiceField(required=False,choices = TRI_CHOICES, label="", initial='', widget=forms.Select(attrs={'class' :"custom-select"}))
    groupe = forms.ModelChoiceField(required=False,queryset=Groupe.objects.all(),empty_label="Groupe",widget=forms.Select(attrs={'class' :"custom-select"}))
    
    def __init__(self, *args, **kwargs):
        promotion = kwargs.pop('promotion', None)
        super().__init__(*args, **kwargs)
        
        if promotion:
            self.fields['groupe'].queryset = Groupe.objects.filter(promotion=promotion).distinct()

class EtudiantImportForm(forms.Form):
    file = forms.FileField()
    
    def process_form(self,request):
        
        promotion=self.fields["promotion"]
        
        input_excel = request.FILES["file"]
        workbook = xlrd.open_workbook(file_contents=input_excel.read())
        
        sheet = workbook.sheet_by_index(0)
        nb_rows=sheet.nrows
        
        for num_row in range(1,nb_rows):
            
            try:
                code_nip=sheet.cell(num_row,0).value
                etudiant,created=Etudiant.objects.get_or_create(code_nip=code_nip)
                etudiant.etudid=sheet.cell(num_row,1).value
                etudiant.nom=sheet.cell(num_row,2).value
                etudiant.prenom=sheet.cell(num_row,4).value
                
                sexe=sheet.cell(num_row,5).value
                if sexe=="MR":
                    sexe="M"
                else:
                    sexe="F"
                etudiant.sexe=sexe
                etudiant.date_naissance=datetime.datetime.strptime(sheet.cell(num_row,6).value, '%d/%m/%Y').strftime('%Y-%m-%d')
                etudiant.lieu_naissance=sheet.cell(num_row,7).value
                etudiant.bac=sheet.cell(num_row,11).value
                etudiant.annee_bac=sheet.cell(num_row,13).value
                etudiant.nomlycee=sheet.cell(num_row,28).value
                etudiant.villelycee=sheet.cell(num_row,29).value
                etudiant.codelycee=sheet.cell(num_row,31).value
                etudiant.email = sheet.cell(num_row,32).value
                etudiant.domicile=sheet.cell(num_row,34).value
                etudiant.codepostaldomicile=sheet.cell(num_row,35).value
                etudiant.villedomicile=sheet.cell(num_row,36).value
                etudiant.paysdomicile=sheet.cell(num_row,37).value
                etudiant.telephone=sheet.cell(num_row,38).value
                etudiant.telephonemobile=sheet.cell(num_row,39).value
                etudiant.save()
                affectation, created=Affectation_Etudiant.objects.get_or_create(etudiant=etudiant,promotion=promotion)
                Bulletin.objects.get_or_create(affectation=affectation,moyenne=0)
            except:
                print ("Unexpected error:", sys.exc_info()[0])
                raise
        
        return self



class AffectationEtudiantForm(forms.ModelForm):
    
    class Meta:
        model = Affectation_Etudiant
        fields=["parcours"]
    
    groupe_cours=forms.ModelChoiceField(queryset=Groupe.objects.filter(type="C"))
    groupe_td=forms.ModelChoiceField(queryset=Groupe.objects.filter(type="TD"))
    groupe_tp=forms.ModelChoiceField(queryset=Groupe.objects.filter(type="TP"))




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


class BulletinImportForm(forms.Form):
    
    fichier_scodoc = forms.FileField()
    
    def process_form(self,request):
        
        input_excel = request.FILES["fichier_scodoc"]
        workbook = xlrd.open_workbook(file_contents=input_excel.read())
        
        promotion=self.fields["promotion"]
        
        sheet = workbook.sheet_by_index(0)
        nb_rows=sheet.nrows
        first_row=sheet.row(0)
        
        #on parcours l'ensemble de la premiere ligne à la recherche des modules
        dict={}
        for col,value in enumerate(first_row):
            
            try:
                module=Module.objects.get(ue__formation=promotion.formation,code_scodoc=value.value)
                dict[col]=module
            except:
                #print ("Unexpected error:", sys.exc_info()[0])
                pass
    
    
        for num_row in range(1,nb_rows-5):
            code_nip=sheet.cell(num_row,1).value
            affectation=Affectation_Etudiant.objects.get(etudiant__code_nip=code_nip,promotion=promotion)
            bulletin=Bulletin.objects.get(affectation__etudiant__code_nip=code_nip,affectation__promotion=promotion)
            bulletin.moyenne=sheet.cell(num_row,6).value
            bulletin.save()
            
            for key in dict:
                module=dict[key]
                moyenne=sheet.cell(num_row,key).value
                if isinstance(moyenne, float):
                    note, created=Note.objects.get_or_create(bulletin=bulletin,module=module)
                    note.moyenne=moyenne
                    note.save()

        return self


class Rapport_Tuteur_EntrepriseForm(forms.ModelForm):
    
    class Meta:
        model = Rapport_Tuteur_Entreprise
        fields=["nom","deadline"]
    
    contrat_list=forms.ModelMultipleChoiceField(queryset=Contrat.objects.all())


