from django.db import models
from django.shortcuts import get_object_or_404
import os
import datetime
from django.db.models.signals import m2m_changed
from django.apps import apps
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from generic.models import create_user


niveaux = (('BTS', 'BTS'),
           ('DUT','DUT'),
           ('L', 'Licence'),
           ('LP','Licence Pro'),
           ('M','Master'),
           ('MP','Master Pro'))

STATUT_CHOICES = (
                  ('P', 'Permanent'),
                  ('V', 'Vacataire'),
                  )

STATUT_CHOICES_DICT = {'P':'Permanent','V': 'Vacataire'}

# General Function

def get_document_path(instance, filename):
    return os.path.join('documents',str(instance.module.ue.formation.mention_short),str(instance.module.code_scodoc),str(instance.pk), filename)

def get_document4groupe_path(instance,filename):
    return os.path.join('documents',str(instance.affectation_enseignant.pk),str(instance.pk), filename)

def get_grille_path(instance,filename):
    return os.path.join('documents',str(instance.pk),filename)

# Create your models here.


class Etablissement(models.Model):
    nom=models.CharField(max_length=300)
    nom_short=models.CharField(max_length=50)
    directeur=models.ForeignKey("Enseignant")
    profile_directeur=models.ImageField(upload_to = 'photos/directeur/',blank = True, null = True)
    email=models.EmailField(blank = True, null = True)
    telephone=models.CharField(max_length=20,null=True,blank=True)
    
    def __str__(self):
        return self.nom_short

    class Meta:
        verbose_name_plural = "1. Etablissements"


class Departement(models.Model):
    etablissement=models.ForeignKey("Etablissement",blank = True, null = True)
    nom=models.CharField(max_length=300)
    nom_short=models.CharField(max_length=50)
    chef=models.ForeignKey("Enseignant",blank = True, null = True)
    profile_chef=models.ImageField(upload_to = 'photos/chef_de_departement/',blank = True, null = True)
    enseignants=models.ManyToManyField("Enseignant",related_name="departement_enseignant")
    administratifs=models.ManyToManyField("Administratif")
    email=models.EmailField(blank = True, null = True)
    telephone=models.CharField(max_length=20,null=True,blank=True)
    
    def __str__(self):
        return self.nom_short

    def formations_actives(self):
        return Formation.objects.filter(departement=self,active=True)

    class Meta:
        verbose_name_plural = "2. Départements"


class Administratif(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100,null=True)
    photo = models.ImageField(upload_to = 'photos/enseignants/',blank = True, null = True)
    date_naissance = models.DateField(auto_now_add=True)
    employeur= models.CharField(max_length=100,default="UBO")
    role=models.CharField(max_length=300,null=True,blank=True)
    email=models.EmailField(blank = True, null = True)
    telephonemobile=models.CharField(max_length=20,blank = True, null = True)
    telephone=models.CharField(max_length=20,null=True,blank=True)
    commentaires=models.TextField(max_length=2000,null=True, blank=True)

    class Meta:
        verbose_name_plural = "5. Administratif"

    def __str__(self):
        return "%s %s" %(self.nom.upper(),self.prenom)

post_save.connect(create_user, sender=Administratif)


class Formation(models.Model):
    departement=models.ForeignKey("Departement",null=True,blank=True)
    responsable=models.ForeignKey("Enseignant",null=True,blank=True,related_name="formation_responsable")
    niveau=models.CharField(max_length=5, choices=niveaux,default='LP')
    domaine=models.CharField(max_length=100)
    mention=models.CharField(max_length=200)
    mention_short=models.CharField(max_length=100,null=True,blank=True)
    date_accreditation=models.DateField(null=True,blank=True)
    objectifs=models.TextField(max_length=2000,null=True, blank=True)
    competences=models.TextField(max_length=2000,null=True, blank=True)
    active=models.BooleanField()
    facebook=models.URLField(max_length=200,null=True, blank=True)
    linkedin=models.URLField(max_length=200,null=True, blank=True)
    enseignants=models.ManyToManyField("Enseignant", blank=True)
    entreprises=models.ManyToManyField("entreprises.Entreprise", blank=True)
    tuteur_entreprises=models.ManyToManyField("entreprises.Tuteur_Entreprise", blank=True)
    consigne_projet=models.TextField(null=True, blank=True)
    grille_projet=models.FileField(upload_to=get_grille_path, blank=True, null=True)
    consigne_contrat=models.TextField(null=True, blank=True)
    grille_contrat=models.FileField(upload_to=get_grille_path, blank=True, null=True)
    consigne_feuille_emargement=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.mention_short
    
    def get_active_promotions(self):
        Promotion=apps.get_model("promotions","Promotion")
        return Promotion.objects.filter(formation=self,active=True)
    
    def get_ues(self):
        UE=apps.get_model("formations","UE")
        return UE.objects.filter(formation=self)
    
    class Meta:
        verbose_name_plural = "3. Formations"
        ordering=["-date_accreditation"]

class Parcours(models.Model):
    formation=models.ForeignKey(Formation)
    nom=models.CharField(max_length=200)
    nom_short=models.CharField(max_length=100,null=True,blank=True)
    ues=models.ManyToManyField("UE")

    def __str__(self):
        return str(self.nom_short)

    def nb_modules(self):
        return Module.objects.filter(ue__parcours=self).count()
    
    def nb_heures(self):
        nb_heures=0
        for ue in self.ues.all():
            nb_heures=nb_heures+ue.nb_heures
        return nb_heures
    
    class Meta:
        verbose_name_plural = "4. Parcours"

class UE(models.Model):
    formation=models.ForeignKey(Formation)
    numero=models.IntegerField()
    intitule = models.CharField(max_length=100)
    nb_heures=models.FloatField()
    nb_ects=models.FloatField()
    coefficient=models.FloatField()

    def __str__(self):
        return u"UE %d" % self.numero
    

    def parcours_list(self):
        return ", ".join(self.parcours_set.all().values_list("nom_short",flat=True))

    def affectation_module(self):
        list_object=Module.objects.filter(ue=self.id).order_by('reference')
        return list_object

    class Meta:
        verbose_name_plural = "5. UEs"
        ordering = ["numero"]

class Module(models.Model):
    ue=models.ForeignKey(UE)
    code_apogee=models.CharField(max_length=20,null=True,blank=True)
    code_scodoc=models.CharField(max_length=10,null=True,blank=True)
    obligatoire=models.BooleanField(verbose_name="Obligatoire",default=True)
    intitule = models.CharField(verbose_name="Intitulé du module",max_length=100)
    nb_heures_cours=models.FloatField()
    nb_heures_td=models.FloatField()
    nb_heures_tp=models.FloatField()
    nb_ects=models.FloatField()
    coefficient=models.FloatField()

    objectifs=models.TextField(verbose_name="Objectifs du module",max_length=1000,null=True, blank=True)
    competences_minimales=models.TextField(verbose_name="Compétences Minimales", max_length=400,null=True, blank=True)
    pre_requis=models.TextField(verbose_name="Pré requis",max_length=1000,null=True, blank=True)
    contenu=models.TextField(max_length=2000,null=True, blank=True)
    modalites=models.TextField(verbose_name="Modalité de Mise en Oeuvre",max_length=1000,null=True, blank=True)
    prolongements=models.ManyToManyField("Module",blank=True)
    mots_cles=models.CharField(verbose_name="Mots cles",max_length=200,null=True, blank=True)
    cc=models.BooleanField(verbose_name="Contrôle continu",default=False)
    modification=models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return u"%s: %s" % (self.code_scodoc, self.intitule)
    
    def nb_heures(self):
        return self.nb_heures_cours+self.nb_heures_td+self.nb_heures_tp
    
    def ue_numero(self):
        return u"UE %d" % (self.ue.numero)
    
    def formation(self):
        return str(self.ue.formation)
    
    
    def get_enseignants(self):
        return Enseignant.objects.filter(modules=self).distinct()
    
    def get_active_enseignants(self):
        return Enseignant.objects.filter(affectation_enseignant__module=self,affectation_enseignant__groupe__promotion__active=True).distinct()

    class Meta:
        verbose_name_plural = "6. Modules"
        ordering = ["code_scodoc"]


class Enseignant(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100,null=True)
    photo = models.ImageField(upload_to = 'photos/enseignants/',blank = True, null = True)
    date_naissance = models.DateField(auto_now_add=True)
    statut=models.CharField(max_length=1, choices=STATUT_CHOICES,default='P')
    employeur= models.CharField(max_length=100,default="UBO")
    email=models.EmailField(blank = True, null = True)
    telephonemobile=models.CharField(max_length=20,blank = True, null = True)
    telephone=models.CharField(max_length=20,null=True,blank=True)
    adresse_rue=models.CharField(max_length=100,blank = True, null = True)
    adresse_zip=models.IntegerField(blank = True, null = True)
    adresse_ville=models.CharField(max_length=100,blank = True, null = True)
    contraintes=models.TextField(verbose_name="Contraintes",blank=True,null=True)
    confirmation=models.BooleanField(verbose_name="Confirmation Participation",default=False)
    modules=models.ManyToManyField(Module, through="promotions.Affectation_Enseignant")
    groupes=models.ManyToManyField("promotions.Groupe",through="promotions.Affectation_Enseignant")
    
    def __str__(self):
        return u"%s %s" % (self.nom.upper(), self.prenom)
    
    def get_related_object(self):
        return None
    
    def get_active_module_list(self):
        module_pk=self.affectation_enseignant_set.filter(groupe__promotion__active=True).values_list("module",flat=True).distinct()
        return Module.objects.filter(pk__in=module_pk)
    
    def get_active_projet_tuteure_list(self):
        return self.projet_tuteure_set.filter(actif=True)
    
    def get_active_contrat_list(self):
        return self.contrat_set.filter(affectation__promotion__active=True)
    
    def get_document4groupe_list(self):
        Document4Groupe=apps.get_model("formations","Document4Groupe")
        return Document4Groupe.objects.filter(affectation_enseignant__enseignant=self)
    
    def get_active_promotion_list(self):
        Promotion=apps.get_model("promotions","Promotion")
        promotion_pk=self.affectation_enseignant_set.filter(groupe__promotion__active=True).order_by().values_list("groupe__promotion",flat=True).distinct()

        return Promotion.objects.filter(pk__in=promotion_pk)


    class Meta:
        verbose_name_plural = "4. Enseignants"
        ordering = ["nom",]

class Document4Groupe(models.Model):
    order=models.IntegerField(default=1)
    affectation_enseignant=models.ForeignKey("promotions.Affectation_Enseignant")
    nom=models.CharField(max_length=400)
    file=models.FileField(upload_to=get_document4groupe_path)
    modification=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["affectation_enseignant__module","nom"]

class Document(models.Model):
    order=models.IntegerField(default=1)
    enseignant=models.ForeignKey("Enseignant")
    module=models.ForeignKey("Module")
    nom=models.CharField(max_length=400)
    file=models.FileField(upload_to=get_document_path)
    audience= models.ManyToManyField("promotions.Groupe",blank=True)
    modification=models.DateTimeField(auto_now=True)

class Evaluation(models.Model):
    enseignant=models.ForeignKey("Enseignant")
    module=models.ForeignKey("Module")
    nom=models.CharField(max_length=400)
    audience=models.ForeignKey("promotions.Groupe",blank=True)
    modification=models.DateTimeField(auto_now=True)
    commentaire=models.TextField(verbose_name="Commentaires",blank=True,null=True)
    deadline=models.DateField(blank=True,null=True,default=datetime.datetime.now)
    active=models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        for etudiant in self.audience.etudiants.all():
            devoir,trash=Devoir.objects.get_or_create(evaluation=self,etudiant=etudiant)
            devoir.changed=False
            devoir.save()

def get_devoir_path(instance, filename):
    return os.path.join('documents',str(instance.evaluation.module.ue.formation.mention_short),str(instance.evaluation.module.code_scodoc),str(instance.evaluation),str(instance.pk), filename)

class Devoir(models.Model):
    evaluation=models.ForeignKey("Evaluation")
    #etudiant=models.ForeignKey("promotions.Etudiant")
    exercice1=models.FileField(upload_to=get_devoir_path,null=True, blank=True)
    exercice2=models.FileField(upload_to=get_devoir_path,null=True, blank=True)
    exercice3=models.FileField(upload_to=get_devoir_path,null=True, blank=True)
    exercice4=models.FileField(upload_to=get_devoir_path,null=True, blank=True)
    exercice5=models.FileField(upload_to=get_devoir_path,null=True, blank=True)
    commentaire=models.TextField(max_length=400,null=True, blank=True)
    modification=models.DateTimeField(auto_now=True)
    changed=models.BooleanField(default=False)



