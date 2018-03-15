from django.conf.urls import url
from . import views



urlpatterns = [
               url(r'^projet_tuteure/(?P<pk>\d+)/detail/$', views.Projet_TuteureDetailView.as_view()),
               url(r'^suivi_projet/(?P<pk>\d+)/detail/$', views.Suivi_ProjetDetailView.as_view()),
               ]
