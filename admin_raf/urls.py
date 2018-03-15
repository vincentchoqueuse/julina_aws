from django.conf.urls import url
from django.contrib.auth.decorators import login_required
#admin_raf view
import formations.admin_raf as view_form
import promotions.admin_raf as view_prom


urlpatterns = [
               ## FORMATION
               url(r'^formation/(?P<formation>\d+)/detail/$',view_form.FormationView.as_view()),
               url(r'^formation/(?P<formation>\d+)/reseau/update/$',view_form.ReseauUpdateView.as_view()),
               url(r'^formation/(?P<formation>\d+)/consigne/$',view_form.ConsigneView.as_view()),
               url(r'^formation/(?P<formation>\d+)/consigne_projet/update/$',view_form.Consigne_Projet_UpdateView.as_view()),
               url(r'^formation/(?P<formation>\d+)/consigne_contrat/update/$',view_form.Consigne_Contrat_UpdateView.as_view()),
               url(r'^formation/(?P<formation>\d+)/consigne_feuille_emargement/update/$',view_form.Consigne_Feuille_UpdateView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/create/$', view_form.PromotionCreateView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<pk>\d+)/update/$', view_form.PromotionUpdateView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<pk>\d+)/delete/$', view_form.PromotionDeleteView.as_view()),
               url(r'^formation/(?P<formation>\d+)/ue/create/$', view_form.UECreateView.as_view()),
               url(r'^formation/(?P<formation>\d+)/ue/(?P<pk>\d+)/update/$', view_form.UEUpdateView.as_view()),
               url(r'^formation/(?P<formation>\d+)/ue/(?P<pk>\d+)/delete/$', view_form.UEDeleteView.as_view()),
               url(r'^formation/(?P<formation>\d+)/module/$', view_form.ModuleView.as_view()),
               url(r'^formation/(?P<formation>\d+)/module/create/$', view_form.ModuleCreateView.as_view()),
               url(r'^formation/(?P<formation>\d+)/module/(?P<pk>\d+)/update/$', view_form.ModuleUpdateView.as_view()),
               url(r'^formation/(?P<formation>\d+)/module/(?P<pk>\d+)/delete/$', view_form.ModuleDeleteView.as_view()),
               url(r'^formation/(?P<formation>\d+)/parcours/$', view_form.ParcoursView.as_view()),
               url(r'^formation/(?P<formation>\d+)/parcours/create/$', view_form.ParcoursCreateView.as_view()),
               url(r'^formation/(?P<formation>\d+)/parcours/(?P<pk>\d+)/update/$', view_form.ParcoursUpdateView.as_view()),
               url(r'^formation/(?P<formation>\d+)/parcours/(?P<pk>\d+)/delete/$', view_form.ParcoursDeleteView.as_view()),
 
               ## PROMOTION
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/detail/$', view_prom.PromotionDetailView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/bulletin/import/$', view_prom.PromotionBulletinImportView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/groupe/create/$', view_prom.GroupeCreateView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/groupe/(?P<pk>\d+)/update/$', view_prom.GroupeUpdateView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/groupe/(?P<pk>\d+)/delete/$', view_prom.GroupeDeleteView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/affectation_enseignant/$', view_prom.Affectation_EnseignantView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/affectation_enseignant/create/$', view_prom.Affectation_EnseignantCreateView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/affectation_enseignant/(?P<pk>\d+)/update/$', view_prom.Affectation_EnseignantUpdateView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/affectation_enseignant/(?P<pk>\d+)/delete/$', view_prom.Affectation_EnseignantDeleteView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/affectation_etudiant/$', view_prom.Affectation_EtudiantView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/affectation_etudiant/(?P<pk>\d+)/update/$', view_prom.Affectation_EtudiantUpdateView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/affectation_etudiant/(?P<pk>\d+)/delete/$', view_prom.Affectation_EtudiantDeleteView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/projet_tuteure/$', view_prom.ProjetListView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/projet_tuteure/create/$', view_prom.Projet_TuteureCreateView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/projet_tuteure/(?P<pk>\d+)/update/$', view_prom.Projet_TuteureUpdateView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/projet_tuteure/(?P<pk>\d+)/delete/$', view_prom.Projet_TuteureDeleteView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/contrat/$', view_prom.ContratView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/contrat/create/$', view_prom.ContratCreateView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/import_contrat/$', view_prom.ContratImportView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/contrat/(?P<pk>\d+)/update/$', view_prom.ContratUpdateView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/contrat/(?P<pk>\d+)/delete/$', view_prom.ContratDeleteView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/calendrier_hebdomadaire/$', view_prom.CalendrierView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/calendrier/create/$', view_prom.CalendrierCreateView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/calendrier/(?P<pk>\d+)/update/$', view_prom.CalendrierUpdateView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/calendrier/(?P<pk>\d+)/delete/$', view_prom.CalendrierDeleteView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/calendrier_hebdomadaire/create/$', view_prom.Calendrier_HebdomadaireCreateView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/calendrier_hebdomadaire/(?P<pk>\d+)/update/$', view_prom.Calendrier_HebdomadaireUpdateView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/calendrier_hebdomadaire/(?P<pk>\d+)/delete/$', view_prom.Calendrier_HebdomadaireDeleteView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/rapport_tuteur_entreprise/$', view_prom.Rapport_Tuteur_EntrepriseView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/rapport_tuteur_entreprise/create/$', view_prom.Rapport_Tuteur_EntrepriseFormView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/rapport_tuteur_entreprise/(?P<pk>\d+)/update/$', view_prom.Rapport_Tuteur_EntrepriseUpdateView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/rapport_tuteur_entreprise/(?P<pk>\d+)/delete/$', view_prom.Rapport_Tuteur_EntrepriseDeleteView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/absence/$', view_prom.AbsenceView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/absence/create/$', view_prom.AbsenceCreateView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/absence/(?P<pk>\d+)/update/$', view_prom.AbsenceUpdateView.as_view()),
               url(r'^formation/(?P<formation>\d+)/promotion/(?P<promotion>\d+)/absence/(?P<pk>\d+)/delete/$', view_prom.AbsenceDeleteView.as_view()),
               
               ]





