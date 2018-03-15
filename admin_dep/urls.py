from django.conf.urls import url
from . import views


urlpatterns= [
              url(r'^(?P<pk>\d+)/detail/$',views.DepartementDetailView.as_view(),name="admin_dep_departement_detail"),
              url(r'^promotion/(?P<pk>\d+)/$',views.PromotionDetailView.as_view()),
              #url(r'^(?P<pk>\d+)/update/$',views.DepartementUpdateView.as_view()),
              ]
