from django.db import models
from formations.models import Formation, Parcours, Document, Devoir
from datetime import datetime
from django.db.models import Sum
from django.apps import apps
import os
from isoweek import Week
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from generic.models import create_user


# Create your models here.

type_groupes = (
            ('C','Cours'),
            ('TD', 'TD'),
           ('TP','TP'),
           ('A', 'Autres'),
           )

choix_sexe = (        ('F', 'Feminin'),
                  ('M', 'Masculin'),
        
                  )


class Promotion(models.Model):
    responsable = models.ForeignKey("formations.Enseignant")
    formation=models.ForeignKey(Formation)
    annee=models.IntegerField(default=datetime.today().year)
    rentree=models.DateField(null=True,blank=True, default='2017-09-01')
    active=models.BooleanField(default=False)
    etudiants=models.ManyToManyField("Etudiant", through='Affectation_Etudiant')

    def __str__(self):
        return "%s %s" %(self.formation.mention_short,self.annee,)
    
    def nom(self):
        return "%s %d" %(self.formation,self.annee)
    
    def get_contrat_list(self):
        Contrat=apps.get_model("entreprises","Contrat")
        return Contrat.objects.filter(affectation__promotion=self)

    def get_affectation_enseignant_list(self):
        Affectation_Enseignant=apps.get_model("promotions","Affectation_Enseignant")
        return Affectation_Enseignant.objects.filter(groupe__promotion=self)
    
    def get_affectation_etudiant_list(self):
        Affectation_Etudiant=apps.get_model("promotions","Affectation_Etudiant")
        return Affectation_Etudiant.objects.filter(promotion=self)
    
    def get_projet_tuteure_list(self):
        Projet_Tuteure=apps.get_model("projets","Projet_Tuteure")
        return Projet_Tuteure.objects.filter(promotion=self)
    
    def get_rapport_tuteur_entreprise_list(self):
        Rapport_Tuteur_Entreprise=apps.get_model("entreprises","Rapport_Tuteur_Entreprise")
        return Rapport_Tuteur_Entreprise.objects.filter(contrat__affectation__promotion=self)
    
    def get_absence_list(self):
        Absence=apps.get_model("promotions","Absence")
        return Absence.objects.filter(affectation_etudiant__promotion=self)
    
    class Meta:
        verbose_name_plural = "1. Promotions"
        ordering = ['-rentree']


def get_image_path():
    return 1

class Etudiant(models.Model):
    user = models.OneToOneField(User,blank=True, null=True, on_delete=models.SET_NULL)
    code_nip=models.CharField(max_length=50,null=True, blank=True)
    photo = models.ImageField(upload_to = "etudiants/", blank=True, null=True)
    etudid= models.CharField(max_length=20,null=True, blank=True)
    etat= models.CharField(max_length=10,null=True, blank=True)
    nom=models.CharField(max_length=30)
    nom_usuel=models.CharField(max_length=30,null=True, blank=True)
    sexe=models.CharField(max_length=10,null=True, blank=True, choices=choix_sexe,default='M')
    prenom=models.CharField(max_length=30)
    inscriptionstr=models.CharField(max_length=30,null=True, blank=True)
    email = models.EmailField(max_length=70,blank=True)
    email_perso = models.EmailField(max_length=70,null=True,blank=True)
    domicile=models.CharField(max_length=100,null=True, blank=True)
    villedomicile=models.CharField(max_length=100,null=True, blank=True)
    codepostaldomicile=models.IntegerField(null=True, blank=True)
    paysdomicile=models.CharField(max_length=100,null=True, blank=True)
    telephone=models.CharField(max_length=20,null=True, blank=True)
    telephonemobile=models.CharField(max_length=20,null=True, blank=True)
    date_naissance=models.CharField(max_length=30,null=True, blank=True, default='2017-09-01')
    lieu_naissance=models.CharField(max_length=30,null=True, blank=True)
    bac=models.CharField(max_length=30,null=True, blank=True)
    bac2=models.CharField(max_length=30,null=True, blank=True)
    specialite=models.CharField(max_length=30,null=True, blank=True)
    annee_bac=models.IntegerField(null=True, blank=True)
    annee_bac2=models.IntegerField(null=True, blank=True)
    nomlycee=models.CharField(max_length=100,null=True, blank=True)
    villelycee=models.CharField(max_length=100,null=True, blank=True)
    codepostallycee=models.IntegerField(null=True, blank=True)
    codelycee=models.CharField(max_length=20,null=True, blank=True)
    etablissement_bac2=models.CharField(max_length=20,null=True, blank=True)
    type_admission=models.CharField(max_length=20,null=True, blank=True)
    boursier_prec=models.CharField(max_length=20,null=True, blank=True)
    debouche=models.CharField(max_length=20,null=True, blank=True)

    def __str__(self):
        return "%s %s" %(self.nom.upper(),self.prenom)
    
    def nom_prenom(self):
        return "%s %s" %(self.nom,self.prenom)
    
    def get_documents(self):
        return None

    def get_devoirs(self):
        return Devoir.objects.filter(etudiant=self,evaluation__active=True)
    
    def get_affectation_list(self):
        return Affectation_Etudiant.objects.filter(etudiant=self)
    
    def get_contrat_list(self):
        Contrat=apps.get_model("entreprises","Contrat")
        return Contrat.objects.filter(affectation__etudiant=self)

    def get_projet_tuteure_list(self):
        Projet_Tuteure=apps.get_model("projets","Projet_Tuteure")
        return Projet_Tuteure.objects.filter(affectation__etudiant=self)
    
    def get_calendrier_list(self):
        Calendrier_Hebdomadaire=apps.get_model("promotions","Calendrier_Hebdomadaire")
        return Calendrier_Hebdomadaire.objects.filter(responsable__etudiant=self)

    class Meta:
        verbose_name_plural = "1. Etudiants"
        ordering=["nom"]

post_save.connect(create_user, sender=Etudiant)


class Groupe(models.Model):
    promotion=models.ForeignKey(Promotion)
    nom=models.CharField(max_length=200,null=True, blank=True)
    type=models.CharField(max_length=5, choices=type_groupes,default='C')
    affectations=models.ManyToManyField("Affectation_Etudiant")
    
    def __str__(self):
        return "%s" %self.nom
    
    def active(self):
        return self.promotion.active
    
    def nb_etudiants(self):
        return self.affectations.count()
    
    
    class Meta:
        verbose_name_plural = "3. Groupes"
        ordering=["nom"]


class Affectation_Etudiant(models.Model):
    etudiant=models.ForeignKey(Etudiant, related_name='affectation_set')
    promotion=models.ForeignKey(Promotion,related_name='promotion_set')
    parcours=models.ForeignKey("formations.Parcours",null=True, blank=True)
    bulletin_visible=models.BooleanField(verbose_name="Communication du bulletin au tuteur entreprise",default=False)

    def __str__(self):
        return "%s" % self.etudiant
    
    def get_document_list(self):
        Document4Groupe=apps.get_model("formations","Document4Groupe")
        return Document4Groupe.objects.filter(affectation_enseignant__groupe__in=self.groupe_set.all())
    
    def get_calendrier(self):
        groupe=Groupe.objects.filter(affectations=self,type="TP").first()
        return Calendrier.objects.filter(groupe=groupe).first()
    
    
    class Meta:
        verbose_name_plural = "4. Affectation Etudiant"
        ordering=["etudiant__nom"]

class Bulletin(models.Model):
    affectation=models.OneToOneField(Affectation_Etudiant)
    modification=models.DateTimeField(auto_now=True)
    moyenne=models.FloatField()
    
    def __str__(self):
        return str(self.affectation.etudiant)

class Note(models.Model):
    bulletin=models.ForeignKey(Bulletin)
    module=models.ForeignKey("formations.Module")
    moyenne=models.FloatField(default=0)

class Affectation_Enseignant(models.Model):
    enseignant=models.ForeignKey("formations.Enseignant", related_name='affectation_enseignant_set',null=True, blank=True)
    module=models.ForeignKey("formations.Module", related_name='affectation_module')
    groupe=models.ForeignKey("Groupe", related_name='affectation_groupe_set')
    commentaire=models.TextField(max_length=400,null=True, blank=True)
    nb_heures=models.FloatField()
    
    def active(self):
        return self.groupe.active
    
    def __str__(self):
        return "%s - %s - %s" % (self.module.code_scodoc, self.groupe, self.enseignant)
    
    def is_complete(self):
        nb_heures_cours_ref=self.module.nb_heures_cours
        nb_heures_td_ref=self.module.nb_heures_td
        nb_heures_tp_ref=self.module.nb_heures_tp
        
        is_complete=1
        
        for groupe in Groupe.objects.filter(promotion=self.groupe.promotion):
            
            nb_heures_ref=0
            if groupe.type=="C":
                nb_heures_ref=self.module.nb_heures_cours
            if groupe.type=="TD":
                nb_heures_ref=self.module.nb_heures_td
            if groupe.type=="TP":
                nb_heures_ref=self.module.nb_heures_tp
            
            aff=Affectation_Enseignant.objects.filter(module=self.module,groupe=groupe).aggregate(nb_heures=Sum("nb_heures"))
            
            nb_heures=aff["nb_heures"]
            if nb_heures==None:
                nb_heures=0

            is_complete=is_complete*(nb_heures_ref==nb_heures)
        
        return bool(is_complete)
    

    class Meta:
        verbose_name_plural = "4. Affectation Enseignant"
        ordering=["-groupe__promotion__annee","module"]

class Calendrier(models.Model):
    promotion=models.ForeignKey("Promotion")
    ics=models.URLField(verbose_name="Calendrier au format ics pour synchronisation",null=True, blank=True)
    groupe=models.ForeignKey("Groupe")
    commentaire=models.TextField(max_length=400,null=True, blank=True)
    

    def __str__(self):
        return "%s %s" % (self.promotion,self.groupe)

class Calendrier_Hebdomadaire(models.Model):
    calendrier=models.ForeignKey(Calendrier)
    num_semaine=models.IntegerField(default=1)
    annee=models.IntegerField(default=datetime.today().year)
    responsable=models.ForeignKey(Affectation_Etudiant,null=True, blank=True)
    commentaire=models.TextField(max_length=400,null=True, blank=True)
    
    def get_week(self):
        w = Week(self.annee,self.num_semaine)
        return w


    class Meta:
        ordering=["annee","num_semaine"]

choix_statut = (
              ('NJ', 'Non Justifié'),
              ('EC', 'En Cours'),
              ('J', 'Justifié'),
              )

def get_justification_path(instance, filename):
    return os.path.join('documents',str(instance.affectation_etudiant.etudiant.pk),str(instance.pk), filename)

class Absence(models.Model):
    creation=models.DateTimeField(auto_now_add=True)
    affectation_etudiant=models.ForeignKey(Affectation_Etudiant)
    debut=models.DateField(default=datetime.now, blank=True)
    fin=models.DateField(default=datetime.now, blank=True)
    enseignants=models.ManyToManyField("formations.Enseignant", blank=True)
    commentaire_raf=models.TextField(max_length=400,null=True, blank=True)
    commentaire_adm=models.TextField(max_length=400,null=True, blank=True)
    commentaire_ens=models.TextField(max_length=400,null=True, blank=True)
    justification=models.FileField(upload_to=get_justification_path,null=True, blank=True)
    statut=models.CharField(max_length=10,choices=choix_statut,default='NJ')





