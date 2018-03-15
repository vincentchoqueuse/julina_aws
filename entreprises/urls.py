from django.conf.urls import url
from . import views

urlpatterns = [
               url(r'^rapport_tuteur_formation/(?P<pk>\d+)/detail/$', views.Rapport_Tuteur_FormationDetailView.as_view()),
               url(r'^rapport_tuteur_entreprise/(?P<pk>\d+)/detail/$', views.Rapport_Tuteur_EntrepriseDetailView.as_view()),
               url(r'^fiche_liaison/(?P<pk>\d+)/detail/$', views.Fiche_LiaisonDetailView.as_view()),
               url(r'^contrat/(?P<pk>\d+)/detail/$', views.ContratDetailView.as_view()),
               url(r'^entreprise/(?P<pk>\d+)/detail/$', views.EntrepriseDetailView.as_view()),
               url(r'^tuteur/(?P<pk>\d+)/detail/$', views.TuteurDetailView.as_view()),
               #LIST JSON
               url(r'^list.json', views.entreprise_list),
               ]
