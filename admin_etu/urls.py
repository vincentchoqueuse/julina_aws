from django.conf.urls import url

#admin_ens view
import projets.admin_etu as view_proj
import promotions.admin_etu as view_prom
import entreprises.admin_etu as view_entr


urlpatterns= [url(r'^profil/$',view_prom.EtudiantDetailView.as_view()),
              url(r'^profil/update/$',view_prom.EtudiantUpdateView.as_view()),
              url(r'^profil/calendrier/$',view_prom.CalendrierListView.as_view()),
              url(r'^affectation_etudiant/(?P<affectation_etudiant>\d+)/detail/$', view_prom.Affectation_EtudiantDetailView.as_view()),
              url(r'^affectation_etudiant/(?P<affectation_etudiant>\d+)/update/$', view_prom.Affectation_EtudiantUpdateView.as_view()),
              url(r'^affectation_etudiant/(?P<affectation_etudiant>\d+)/document/$', view_prom.DocumentListView.as_view()),
              url(r'^affectation_etudiant/(?P<affectation_etudiant>\d+)/enseignant/$',view_prom.EnseignantListView.as_view()),
              url(r'^affectation_etudiant/(?P<affectation_etudiant>\d+)/etudiant/$', view_prom.EtudiantListView.as_view()),
              url(r'^affectation_etudiant/(?P<affectation_etudiant>\d+)/projet_tuteure/$',view_prom.Projet_TuteureListView.as_view()),
              url(r'^affectation_etudiant/(?P<affectation_etudiant>\d+)/calendrier/$', view_prom.Calendrier2ListView.as_view()),
              url(r'^contrat/(?P<contrat>\d+)/detail/$',view_entr.ContratDetailView.as_view()),
              url(r'^contrat/(?P<contrat>\d+)/fiche_liaison/create/$',view_entr.Fiche_LiaisonCreateView.as_view()),
              url(r'^contrat/(?P<contrat>\d+)/fiche_liaison/(?P<pk>\d+)/update/$',view_entr.Fiche_LiaisonUpdateView.as_view()),
              url(r'^contrat/(?P<contrat>\d+)/entreprise/$',view_entr.EntrepriseDetailView.as_view()),
              url(r'^contrat/(?P<contrat>\d+)/consigne/$',view_entr.ConsigneContratDetailView.as_view()),
              url(r'^projet_tuteure/(?P<projet_tuteure>\d+)/detail/$',view_proj.Projet_TuteureDetailView.as_view()),
              url(r'^projet_tuteure/(?P<projet_tuteure>\d+)/description/$',view_proj.DescriptionDetailView.as_view()),
              url(r'^projet_tuteure/(?P<projet_tuteure>\d+)/consigne/$',view_proj.ConsigneDetailView.as_view()),
              url(r'^projet_tuteure/(?P<projet_tuteure>\d+)/suivi_projet/create/$',view_proj.Suivi_ProjetCreateView.as_view()),
              url(r'^projet_tuteure/(?P<projet_tuteure>\d+)/suivi_projet/(?P<pk>\d+)/update/$',view_proj.Suivi_ProjetUpdateView.as_view()),
              url(r'^projet_tuteure/(?P<projet_tuteure>\d+)/suivi_projet/(?P<pk>\d+)/delete/$',view_proj.Suivi_ProjetDeleteView.as_view()),
            ]
