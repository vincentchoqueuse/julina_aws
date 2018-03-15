from django.conf.urls import url
import formations.views as view_form

import formations.admin as view_form
import promotions.admin as view_prom
import entreprises.admin as view_entr

urlpatterns= [
              #url(r'^absence/$',view_prom.AbsenceListView.as_view()),
              #url(r'^absence/(?P<pk>\d+)/update/$',view_prom.AbsenceUpdateView.as_view()),
              url(r'^formation/$',view_form.FormationListView.as_view()),
              url(r'^formation/create/$',view_form.FormationCreateView.as_view()),
              url(r'^formation/(?P<pk>\d+)/update/$',view_form.FormationUpdateView.as_view()),
              url(r'^formation/(?P<pk>\d+)/delete/$',view_form.FormationDeleteView.as_view()),
              url(r'^enseignant/$',view_form.EnseignantListView.as_view()),
              url(r'^enseignant/export/$',view_form.EnseignantExportView.as_view()),
              url(r'^enseignant/create/$',view_form.EnseignantCreateView.as_view()),
              url(r'^enseignant/(?P<pk>\d+)/update/$',view_form.EnseignantUpdateView.as_view()),
              url(r'^enseignant/(?P<pk>\d+)/delete/$',view_form.EnseignantDeleteView.as_view()),
              url(r'^promotion/$',view_prom.PromotionListView.as_view()),
              url(r'^promotion/create/$',view_prom.PromotionCreateView.as_view()),
              url(r'^promotion/(?P<pk>\d+)/update/$',view_prom.PromotionUpdateView.as_view()),
              url(r'^promotion/(?P<pk>\d+)/delete/$',view_prom.PromotionDeleteView.as_view()),
              url(r'^etudiant/$',view_prom.EtudiantListView.as_view()),
              url(r'^etudiant/create/$',view_prom.EtudiantCreateView.as_view()),
              url(r'^etudiant/(?P<pk>\d+)/update/$',view_prom.EtudiantUpdateView.as_view()),
              url(r'^etudiant/(?P<pk>\d+)/delete/$',view_prom.EtudiantDeleteView.as_view()),
              url(r'^entreprise/$',view_entr.EntrepriseListView.as_view()),
              url(r'^entreprise/export/$',view_entr.EntrepriseExportView.as_view()),
              url(r'^entreprise_carte/$',view_entr.CarteListView.as_view()),
              url(r'^entreprise/create/$',view_entr.EntrepriseCreateView.as_view()),
              url(r'^entreprise/(?P<pk>\d+)/update/$',view_entr.EntrepriseUpdateView.as_view()),
              url(r'^entreprise/(?P<pk>\d+)/delete/$',view_entr.EntrepriseDeleteView.as_view()),
              url(r'^tuteur_entreprise/$',view_entr.Tuteur_EntrepriseListView.as_view()),
              url(r'^tuteur_entreprise/create/$',view_entr.Tuteur_EntrepriseCreateView.as_view()),
              url(r'^tuteur_entreprise/(?P<pk>\d+)/update/$',view_entr.Tuteur_EntrepriseUpdateView.as_view()),
              url(r'^tuteur_entreprise/(?P<pk>\d+)/delete/$',view_entr.Tuteur_EntrepriseDeleteView.as_view()),
              url(r'^rapport_tuteur_formation/$',view_entr.Rapport_Tuteur_FormationListView.as_view()),
              url(r'^rapport_tuteur_formation/create/$',view_entr.Rapport_Tuteur_FormationCreateView.as_view()),
              url(r'^rapport_tuteur_formation/(?P<pk>\d+)/update/$',view_entr.Rapport_Tuteur_FormationUpdateView.as_view()),
              url(r'^rapport_tuteur_formation/(?P<pk>\d+)/delete/$',view_entr.Rapport_Tuteur_FormationDeleteView.as_view()),
              url(r'^rapport_tuteur_entreprise/$',view_entr.Rapport_Tuteur_EntrepriseListView.as_view()),
              url(r'^rapport_tuteur_entreprise/create/$',view_entr.Rapport_Tuteur_EntrepriseCreateView.as_view()),
              url(r'^rapport_tuteur_entreprise/(?P<pk>\d+)/update/$',view_entr.Rapport_Tuteur_EntrepriseUpdateView.as_view()),
              url(r'^rapport_tuteur_entreprise/(?P<pk>\d+)/delete/$',view_entr.Rapport_Tuteur_EntrepriseDeleteView.as_view()),
              ]

