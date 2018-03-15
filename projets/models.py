from django.db import models

# Create your models here.


class Projet_Tuteure(models.Model):
    modification=models.DateTimeField(auto_now_add=True)
    promotion=models.ForeignKey("promotions.Promotion")
    intitule = models.CharField(verbose_name="Intitulé du Projet",max_length=100)
    enseignant=models.ForeignKey("formations.Enseignant")
    affectation=models.ManyToManyField("promotions.Affectation_Etudiant", blank=True)
    salle=models.CharField(max_length=100,null=True, blank=True)
    contexte=models.TextField(verbose_name="Contexte du Projet",null=True, blank=True)
    problematique=models.TextField(verbose_name="Problématique",null=True, blank=True)
    methodologie=models.TextField(verbose_name="Méthodologie",null=True, blank=True)
    remarque=models.TextField(verbose_name="Remarques",null=True, blank=True)
    actif=models.BooleanField(verbose_name="Projet en cours",default=False)
    

    def etudiants(self):
        return ', '.join([str(affectation.etudiant) for affectation in self.affectation.all()])
 
 
    def is_affected(self):
        nb_etudiants=self.affectation.count()
        return nb_etudiants>0
    
    def __str__(self):
        return u"%s" % (self.intitule)
    
 
    class Meta:
        verbose_name_plural = "4. Projet Tuteurés"
        ordering=["-actif"]


class Suivi_Projet(models.Model):
    projet=models.ForeignKey(Projet_Tuteure)
    date=models.DateTimeField(auto_now=True)
    nombre_heures=models.IntegerField()
    travail_effectue=models.TextField(verbose_name="Travail effectué")
    difficultes=models.TextField(verbose_name="Difficultés rencontrées")
    suite=models.TextField(verbose_name="Suite envisagée")
    remarques=models.TextField(verbose_name="Remarque de l’enseignant")

    class Meta:
        ordering=["-date"]


class Jury_Projet(models.Model):
    projet=models.OneToOneField(Projet_Tuteure,primary_key=True)
    accesseur=models.ForeignKey("formations.Enseignant",null=True, blank=True)
    horaire=models.DateTimeField(null=True, blank=True)
    salle = models.CharField(max_length=10,null=True, blank=True)
    




