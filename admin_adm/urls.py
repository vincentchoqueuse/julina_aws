from django.conf.urls import url
from . import views
import formations.admin_adm as view_form
import promotions.admin_adm as view_prom

urlpatterns= [
              #PROFIL
              url(r'^profil/$',view_form.AdministratifDetailView.as_view(),name="admin_ens_enseignant_detail"),
              url(r'^profil/update/$', view_form.AdministratifUpdateView.as_view()),
              
              url(r'^absence/$',views.AbsenceListView.as_view()),
              url(r'^absence/(?P<pk>\d+)/update/$',views.AbsenceUpdateView.as_view()),
              url(r'^enseignant/$',views.EnseignantListView.as_view()),
              url(r'^enseignant/(?P<pk>\d+)/update/$',views.EnseignantUpdateView.as_view()),
              url(r'^promotion/(?P<promotion>\d+)/affectation_etudiant/$',view_prom.Affectation_EtudiantListView.as_view()),
              url(r'^promotion/(?P<promotion>\d+)/affectation_enseignant/$',view_prom.Affectation_EnseignantListView.as_view()),
              url(r'^promotion/(?P<promotion>\d+)/projet_tuteure/$',view_prom.Projet_TuteureListView.as_view()),
              url(r'^promotion/(?P<promotion>\d+)/contrat/$',view_prom.ContratListView.as_view()),
              url(r'^promotion/(?P<promotion>\d+)/detail/$',view_prom.PromotionDetailView.as_view()),
              url(r'^promotion/(?P<promotion>\d+)/emargement/$',view_prom.EmargementListView.as_view()),
              url(r'^promotion/(?P<promotion>\d+)/absence/$',view_prom.AbsenceListView.as_view()),
              url(r'^promotion/(?P<promotion>\d+)/absence/create/$',view_prom.AbsenceCreateView.as_view()),
              url(r'^promotion/(?P<promotion>\d+)/absence/(?P<pk>\d+)/update/$',view_prom.AbsenceUpdateView.as_view()),
              url(r'^promotion/(?P<promotion>\d+)/absence/(?P<pk>\d+)/delete/$',view_prom.AbsenceDeleteView.as_view()),
              ]


