from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.apps import apps
import unidecode


def create_user(sender, instance, created, **kwargs):
    if created:
        nom_base=unidecode.unidecode(instance.nom).lower().rstrip().replace(" ", "_")
        nom=nom_base
        value=1
        while User.objects.filter(username=nom).count() > 0:
            nom="%s_%d" %(nom_base,value)
            value=value+1
    
        if isinstance(instance, apps.get_model("promotions","Etudiant")):
            password="iut_brest"
            email=instance.email_perso
            nom="e%s" % instance.code_nip
        if isinstance(instance, apps.get_model("formations","Administratif")):
            password="geii6068"
            email=instance.email
        if isinstance(instance,apps.get_model("entreprises","Tuteur_Entreprise")):
            password="iut_brest_tuteur"
            email=instance.email
        if isinstance(instance,apps.get_model("formations","Enseignant")):
            password="geii6068"
            email=instance.email
        
        user = User.objects.create_user(username=nom,email=email,password=password)
        instance.user=user
        instance.save()
