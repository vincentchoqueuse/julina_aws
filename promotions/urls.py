from django.conf.urls import url
from . import views


urlpatterns = [
               url(r'^promotion/(?P<pk>\d+)/detail/$', views.PromotionDetailView.as_view()),
               url(r'^groupe/(?P<pk>\d+)/detail/$', views.GroupeDetailView.as_view()),
               url(r'^affectation_etudiant/(?P<pk>\d+)/detail/$', views.Affectation_EtudiantDetailView.as_view()),
               url(r'^etudiant/(?P<pk>\d+)/detail/$', views.EtudiantDetailView.as_view()),
               url(r'^calendrier/(?P<pk>\d+)/detail/$', views.CalendrierDetailView.as_view()),
               url(r'^bulletin/(?P<pk>\d+)/detail/$', views.BulletinDetailView.as_view()),
               url(r'^absence/(?P<pk>\d+)/detail/$', views.AbsenceDetailView.as_view()),

               ]
