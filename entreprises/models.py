from django.db import models
import json, requests
import datetime
import os
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from generic.models import create_user

NOTE = (
        (4, 'Excellent'),
        (3, 'Très Bon'),
        (2,'Bon'),
        (1,'Passable'),
        (0,'Non Satisfaisant'),
        )

TYPE = (
        ('CP', 'Contrat de Professionnalisation'),
        ('CA', 'Contrat Apprentissage'),
        ('S','Stage'),
        ('Autre','Autre'),
        )

# Create your models here.

def get_image_path(instance, filename):
    return os.path.join("entreprises", str(instance.siret), filename)

class Entreprise(models.Model):

    siret=models.BigIntegerField(primary_key=True,default=1)
    profile_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    nom=models.CharField(max_length=100,blank=True,null=True)
    statut=models.CharField(max_length=100,blank=True,null=True)
    naf=models.CharField(max_length=100,blank=True,null=True)
    depet=models.IntegerField(blank=True,null=True)
    activite=models.CharField(max_length=300,blank=True,null=True)
    adresse_rue=models.CharField(max_length=100,blank=True,null=True)
    adresse_zip=models.IntegerField(blank=True,null=True)
    adresse_ville=models.CharField(max_length=200,blank=True,null=True)
    gps_lat=models.FloatField(default=0)
    gps_long=models.FloatField(default=0)
    contrats= models.ManyToManyField("Contrat",related_name="contrat",blank=True)
    website=models.URLField(blank=True,null=True)

    def __str__(self):
        return "%s" %self.nom
    
    class Meta:
        verbose_name_plural = "1. Entreprise"
        ordering=["nom"]

    def nb_contrats(self):
        return len(Contrat.objects.filter(entreprise=self).all())
    
    def last_contrat(self):
        last=""
        contrats=Contrat.objects.filter(entreprise=self).order_by('-affectation__promotion__annee')
        if contrats:
            last=contrats[0].affectation.promotion.annee
        return last
    
    def save(self, *args, **kwargs):
        if not(self.nom):
            self.nomen_long="None"
            try:
                url="https://data.opendatasoft.com/api/records/1.0/search/?dataset=sirene%%40public&q=siret%%3D%d&facet=categorie&facet=proden&facet=libapen&facet=siege&facet=libreg_new&facet=saisonat&facet=libtefen&facet=depet&facet=libnj&facet=libtca&facet=liborigine" % self.siret
            
                fields=["depet","l1_normalisee","l4_normalisee","l6_normalisee","l7_normalisee","apet700","libapen","nomen_long","libtefet"]

                resp = requests.get(url=url)
                data = json.loads(resp.text)
                data = data["records"][0]["fields"]

                for field in fields:
                    if field in data:
                        setattr(self,field,data[field])
            except:
                pass

        super().save(*args, **kwargs)


class Responsable_Administratif(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100,null=True)
    poste = models.CharField(max_length=200,null=True)
    email=models.EmailField(blank = True, null = True)
    telephonemobile=models.CharField(max_length=20,blank = True, null = True)
    remarques=models.TextField(verbose_name="Remarques",max_length=400,null=True, blank=True)

    def __str__(self):
        return "%s %s" %(self.nom,self.prenom)

class Tuteur_Entreprise(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100,null=True)
    poste = models.CharField(max_length=200,blank = True, null = True)
    email=models.EmailField(blank = True, null = True)
    telephonemobile=models.CharField(max_length=20,blank = True, null = True)
    remarques=models.TextField(verbose_name="Remarques",max_length=400,null=True, blank=True)

    def __str__(self):
        return "%s %s" %(self.nom,self.prenom)

    def entreprises(self):
        return Contrat.objects.filter(tuteur_entreprise=self).values_list('entreprise__nom', flat=True).distinct()

    

    class Meta:
        verbose_name_plural = "2. Tuteur Entreprise"
        ordering=["nom"]


post_save.connect(create_user, sender=Tuteur_Entreprise)


class CQPM(models.Model):
    numero=models.IntegerField()
    intitule=models.CharField(max_length=100,blank = True, null = True)
    description=models.CharField(max_length=200,blank = True, null = True)

    def __str__(self):
        return "CQPM %s: %s" %(self.numero,self.intitule)

class Contrat(models.Model):
    type=models.CharField(max_length=100,null=True,choices=TYPE)
    affectation=models.ForeignKey("promotions.Affectation_Etudiant",blank = True, null = True)
    responsable_administratif=models.ForeignKey(Responsable_Administratif,blank = True, null = True)
    intitule=models.CharField(max_length=400,blank = True, null = True)
    tuteur_formation=models.ForeignKey("formations.Enseignant",blank = True, null = True)
    tuteur_entreprise=models.ForeignKey(Tuteur_Entreprise,blank = True, null = True)
    entreprise=models.ForeignKey(Entreprise,blank = True, null = True)
    opca=models.CharField(max_length=200,blank=True,null=True)
    remarques=models.TextField(verbose_name="Remarques",max_length=400,null=True, blank=True)
    cqpm=models.ForeignKey(CQPM,blank = True, null = True)

    def __str__(self):
        return "%s_%s" %(self.affectation.etudiant.nom,self.entreprise)
    
    def get_rapport_tuteur_entreprise_list(self):
        return Rapport_Tuteur_Entreprise.objects.filter(contrat=self)
    
    def tuteur_nb_affectation(self):
        return Contrat.objects.filter(affectation__promotion__active=True,tuteur_formation=self.tuteur_formation).count()
    
    
    class Meta:
        verbose_name_plural = "2. Contrats"
        ordering=["entreprise","-affectation__promotion__annee"]


class Fiche_Liaison(models.Model):
    """ Fiche completée par les étudiants" """
    

    contrat=models.OneToOneField(Contrat)
    date_modification = models.DateTimeField(auto_now=True)
    nom_tuteur= models.CharField(max_length=100)
    mail_tuteur=models.EmailField()
    fonction_tuteur= models.CharField(max_length=100)
    telephone_tuteur=models.CharField(max_length=30,blank = True, null = True)
    intitule=models.CharField(verbose_name="Intitulé du stage (en quelques mots)",max_length=300)
    adresse_stage=models.CharField(verbose_name="Adresse de l'entreprise", max_length=200,blank = True, null = True)
    service=models.CharField(verbose_name="Service où le contrat est effectué",max_length=300)
    programme=models.TextField(verbose_name="Objectifs de votre travail présentés lors de votre arrivée")
    impression=models.TextField(verbose_name="Premières impressions sur l'accueil")
    dates_visite=models.TextField(verbose_name="Dates préférentielles pour la visite",help_text="Jours et périodes les plus propices à une visite de l'enseignant ou indisponibilités de tuteur entreprise (si nécessaire) ",default="Pas de préférences")
    problemes=models.TextField(verbose_name="Problèmes qui se posent éventuellement",default="Rien à signaler")
    
    class Meta:
        verbose_name_plural = "3. Information"

class Rapport_Tuteur_Formation(models.Model):
    contrat=models.ForeignKey(Contrat)
    date_visite=models.DateField(help_text="format: année-mois-jours (exemple 2014-03-1)",default=datetime.date.today)
    condition_travail=models.IntegerField(choices=NOTE)
    integration=models.IntegerField(verbose_name="Intégration du stagiaire dans l'entreprise", choices=NOTE)
    activite=models.TextField(verbose_name="Description des activités du stagiaire pendant la période passée")
    visite=models.TextField(verbose_name="Déroulement de la visite, Objets des échanges")
    commentaires=models.TextField(blank=True,null=True)
    
    class Meta:
        verbose_name_plural = "4. Rapports de Visites"
        ordering=["-date_visite"]


class Rapport_Tuteur_Entreprise(models.Model):
    modification=models.DateTimeField(auto_now=True)
    nom=models.CharField(verbose_name="Nom de l'évaluation",max_length=100,default="Evaluation")
    contrat=models.ForeignKey(Contrat)
    deadline=models.DateField(verbose_name="Evaluation à completer avant", help_text="format: année-mois-jours (exemple 2014-03-1)",default=datetime.date.today)
    apprentissage=models.IntegerField(verbose_name="Facilité d'apprentissage",help_text="Aptitude à faire l'acquisition de connaissances ou d'aptitudes nouvelles",choices=NOTE,blank=True,null=True)
    ecoute=models.IntegerField(verbose_name="Ecoute et compréhension",help_text="Réceptivité aux directives et aux conseils fournis par l'encadrement",choices=NOTE,blank=True,null=True)
    curiosite=models.IntegerField(verbose_name="Curiosité",help_text="Intérêt pour le cadre de travail et ce qui s'y fait, indépendamment du travail demandé.",choices=NOTE,blank=True,null=True)
    imagination=models.IntegerField(verbose_name="Imagination pratique",help_text="Aptitude à trouver des solutions originales aux problèmes qui se posent.",choices=NOTE,blank=True,null=True)
    jugement=models.IntegerField(verbose_name="Jugement",help_text="Les avis et choix du stagiaire paraissent-ils sûrs et bien étayés.",choices=NOTE,blank=True,null=True)
    motivation=models.IntegerField(verbose_name="Motivation",help_text="Degré d'intérêt pour le travail demandé.",choices=NOTE,blank=True,null=True)
    methode=models.IntegerField(verbose_name="Méthode - organisation",help_text="Sait mettre en oeuvre les moyens nécessaires à la réalisation de ses objectifs",choices=NOTE,blank=True,null=True)
    autonomie=models.IntegerField(verbose_name="Autonomie",help_text="De 'ne demande conseil qu'à bon escient' à doit 'être tenu par la main'",choices=NOTE,blank=True,null=True)
    qualite=models.IntegerField(verbose_name="Qualité du travail fourni",help_text="De 'a dépassé de loin en quantité et qualité ce qui était attendu' à 'a fourni un résultat très décevant'",choices=NOTE,blank=True,null=True)
    dynamisme=models.IntegerField(verbose_name="Dynamisme et tenacité",help_text="De 'stimulé par les difficultés' à 'abandonne à la première difficulté'",choices=NOTE,blank=True,null=True)
    expression=models.IntegerField(verbose_name="Expression et langage",help_text="Qualité de la communication et de l'expression orale",choices=NOTE,blank=True,null=True)
    relation=models.IntegerField(verbose_name="Relation avec l'entourage",help_text="Le stagiaire est de 'extrêmement apprécié' à 'difficilement admis' par les autres.",choices=NOTE,blank=True,null=True)
    commentaire=models.TextField(verbose_name="Commentaire général sur la prestation en entreprise",blank=True,null=True)
    actif=models.BooleanField(default=True)
    
    def note(self):
        try:
            note=(self.apprentissage+self.ecoute+self.curiosite+self.imagination+self.jugement+self.motivation+self.methode+self.autonomie+self.qualite+self.dynamisme+self.expression+self.relation)+12
            note=round(note/3,2)
        except:
            note=None
        return note
    
    
    class Meta:
        verbose_name_plural = "5. Evaluations"
        ordering=["-deadline"]
