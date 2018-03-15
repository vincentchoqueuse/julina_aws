from django.conf.urls import url
from . import views
import entreprises.admin_tut as view_entr

urlpatterns= [
              url(r'^profil/$',view_entr.TuteurDetailView.as_view()),
              url(r'^profil/update/$',view_entr.TuteurUpdateView.as_view()),
              url(r'^contrat/(?P<pk>\d+)/detail/$',view_entr.ContratDetailView.as_view()),
              url(r'^contrat/(?P<contrat>\d+)/rapport_tuteur_entreprise/(?P<pk>\d+)/update/$',view_entr.Rapport_Tuteur_EntrepriseUpdateView.as_view()),
              url(r'^contrat/(?P<contrat>\d+)/fiche_liaison/$',view_entr.Fiche_LiaisonDetailView.as_view()),
              url(r'^contrat/(?P<contrat>\d+)/rapport_tuteur_formation/$',view_entr.Rapport_Tuteur_FormationListView.as_view()),
              url(r'^contrat/(?P<contrat>\d+)/calendrier_hebdomadaire/$',view_entr.Calendrier_HebdomadaireListView.as_view()),
              url(r'^contrat/(?P<contrat>\d+)/formation/$',view_entr.FormationListView.as_view()),
              ]

