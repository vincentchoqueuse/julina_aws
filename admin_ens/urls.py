from django.conf.urls import url


#admin_ens view
import projets.admin_ens as view_proj
import formations.admin_ens as view_form
import promotions.admin_ens as view_prom
import entreprises.admin_ens as view_entr


base_name="admin_ens"

urlpatterns= [
              #ENSEIGNANT
              url(r'^profil/$',view_form.EnseignantDetailView.as_view(),name="admin_ens_enseignant_detail"),
              url(r'^profil/affectation_enseignant/$',view_form.Affectation_EnseignantListView.as_view()),
              url(r'^profil/affectation_enseignant/(?P<pk>\d+)/update/$',view_form.Affectation_EnseignantUpdateView.as_view()),
              url(r'^profil/contrat/$',view_form.ContratListView.as_view()),
              url(r'^profil/projet_tuteure/$',view_form.Projet_TuteureListView.as_view()),
              url(r'^profil/update/$', view_form.EnseignantUpdateView.as_view()),
        
              ##promotion
              url(r'^promotion/(?P<promotion>\d+)/detail/$',view_prom.PromotionDetailView.as_view()),
              url(r'^promotion/(?P<promotion>\d+)/maquette/$',view_prom.MaquetteListView.as_view()),
              url(r'^promotion/(?P<promotion>\d+)/affectation_etudiant/$',view_prom.Affectation_EtudiantListView.as_view()),
              url(r'^promotion/(?P<promotion>\d+)/contrat/$',view_prom.ContratListView.as_view()),
              url(r'^promotion/(?P<promotion>\d+)/projet_tuteure/$',view_prom.Projet_TuteureListView.as_view()),
              url(r'^promotion/(?P<promotion>\d+)/emargement/$',view_prom.EmargementListView.as_view()),
              url(r'^promotion/(?P<promotion>\d+)/absence/$',view_prom.AbsenceListView.as_view()),
              url(r'^promotion/(?P<promotion>\d+)/absence/create/$',view_prom.AbsenceCreateView.as_view()),
              url(r'^promotion/(?P<promotion>\d+)/document4groupe/$',view_prom.Document4GroupeListView.as_view()),
              url(r'^promotion/(?P<promotion>\d+)/document4groupe/create/$',view_prom.Document4GroupeCreateView.as_view()),
              url(r'^promotion/(?P<promotion>\d+)/document4groupe/(?P<pk>\d+)/update/$',view_prom.Document4GroupeUpdateView.as_view()),
              url(r'^promotion/(?P<promotion>\d+)/document4groupe/(?P<pk>\d+)/delete/$',view_prom.Document4GroupeDeleteView.as_view()),
              url(r'^promotion/(?P<promotion>\d+)/absence/(?P<pk>\d+)/update/$',view_prom.AbsenceUpdateView.as_view()),
              url(r'^promotion/(?P<promotion>\d+)/absence/(?P<pk>\d+)/delete/$',view_prom.AbsenceDeleteView.as_view()),
              
              #contrat
              url(r'^contrat/(?P<contrat>\d+)/detail/$',view_entr.ContratDetailView.as_view()),
              url(r'^contrat/(?P<contrat>\d+)/fiche_liaison/$',view_entr.Fiche_LiaisonDetailView.as_view()),
              url(r'^contrat/(?P<contrat>\d+)/fiche_liaison/update/$',view_entr.Fiche_LiaisonUpdateView.as_view()),
              url(r'^contrat/(?P<contrat>\d+)/bulletin/$',view_entr.BulletinDetailView.as_view()),
              url(r'^contrat/(?P<contrat>\d+)/entreprise/$',view_entr.EntrepriseDetailView.as_view()),
              url(r'^contrat/(?P<contrat>\d+)/contrat/$',view_entr.ContratListView.as_view()),
              url(r'^contrat/(?P<contrat>\d+)/consigne/$',view_entr.ConsigneDetailView.as_view()),
              url(r'^contrat/(?P<contrat>\d+)/calendrier/$',view_entr.CalendrierDetailView.as_view()),
              url(r'^contrat/(?P<contrat>\d+)/rapport_tuteur_formation/create/$',view_entr.Rapport_Tuteur_FormationCreateView.as_view()),
              url(r'^contrat/(?P<contrat>\d+)/rapport_tuteur_formation/(?P<pk>\d+)/update/$',view_entr.Rapport_Tuteur_FormationUpdateView.as_view()),
              url(r'^contrat/(?P<contrat>\d+)/rapport_tuteur_formation/(?P<pk>\d+)/delete/$',view_entr.Rapport_Tuteur_FormationDeleteView.as_view()),
              
              #projet
              url(r'^projet_tuteure/(?P<projet_tuteure>\d+)/detail/$',view_proj.Projet_TuteureDetailView.as_view()),
              url(r'^projet_tuteure/(?P<projet_tuteure>\d+)/projet/$',view_proj.Projet_Tuteure2DetailView.as_view()),
              url(r'^projet_tuteure/(?P<projet_tuteure>\d+)/consigne/$',view_proj.ConsigneDetailView.as_view()),
              url(r'^projet_tuteure/(?P<projet_tuteure>\d+)/projet/update/$',view_proj.Projet_TuteureUpdateView.as_view()),
              url(r'^projet_tuteure/(?P<projet_tuteure>\d+)/suivi_projet/(?P<pk>\d+)/update/$',view_proj.Suivi_ProjetUpdateView.as_view()),
              
 
              ]


