"""julina URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from core.views import IndexPage,LoginRedirectView
from django.http import HttpResponse


# AJAX TO UPDATE session variable


urlpatterns = [
    url(r'^$',LoginRedirectView.as_view(), name='index'),
    url(r'^login/success/',LoginRedirectView.as_view(), name='login_success'),
    url(r'^admin/', admin.site.urls),
    url(r'^formations/', include('formations.urls')),
    url(r'^promotions/', include('promotions.urls')),
    url(r'^projets/', include('projets.urls')),
    url(r'^entreprises/', include('entreprises.urls')),
    url(r'^admin_adm/adm/', include('admin.urls')),
    url(r'^admin_adm/', include('admin_adm.urls')),
    url(r'^admin_ens/', include('admin_ens.urls')),
    url(r'^admin_ens/raf/', include('admin_raf.urls')),
    url(r'^admin_ens/adm/', include('admin.urls')),
    url(r'^admin_etu/', include('admin_etu.urls')),
    url(r'^admin_tut/', include('admin_tut.urls')),
    url(r'^admin_dep/', include('admin_dep.urls')),
    url(r'^login/$', auth_views.login, {'template_name': 'signup.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
