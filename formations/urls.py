from django.conf.urls import url
from . import views

urlpatterns = [
               url(r'^$', views.FormationListView.as_view(), name='formations_list'),
               url(r'^(?P<pk>\d+)$', views.FormationDetailView.as_view(), name='formation_detail'),
               url(r'^(?P<pk>\d+)/consigne_projet/detail/$', views.Consigne_ProjetDetailView.as_view()),
               url(r'^(?P<pk>\d+)/consigne_contrat/detail/$', views.Consigne_ContratDetailView.as_view()),
               url(r'^(?P<pk>\d+)/consigne_feuille_emargement/detail/$', views.Consigne_Feuille_EmargementDetailView.as_view()),
               # DETAIL
               url(r'^departement/(?P<pk>\d+)/detail/$', views.DepartementDetailView.as_view()),
               url(r'^formation/(?P<pk>\d+)/detail/$', views.FormationDetailView.as_view()),
               url(r'^ue/(?P<pk>\d+)/detail/$', views.UEDetailView.as_view()),
               url(r'^module/(?P<pk>\d+)/detail/$', views.ModuleDetailView.as_view()),
               url(r'^parcours/(?P<pk>\d+)/detail/$', views.ParcoursDetailView.as_view()),
               url(r'^enseignant/(?P<pk>\d+)/detail/$', views.EnseignantDetailView.as_view()),


               ]
