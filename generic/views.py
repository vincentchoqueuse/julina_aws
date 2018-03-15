from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.db import models
from django.db.models.fields.related import RelatedField
from django.template.loader import render_to_string
from django.http import JsonResponse,Http404
from django.contrib.auth.mixins import UserPassesTestMixin
from formations.models import Formation
from promotions.models import Promotion

# Pass Test

class UserMixin():

    url_prefix=None
    menu=None
    can_create=False
    can_update=False
    can_delete=False
    can_filter=False
    can_export=False
    nav_template=None
    breadcrumb_template=None
    title=None
    nav_active=None
    sidebar_template=None
    

    
    def get_url_prefix(self):
        return self.url_prefix
    
    def get_nav_active(self):
        if self.nav_active == None:
            nav_active=self.model.__name__.lower()
        else:
            nav_active=self.nav_active
        return nav_active
    
    def get_sidebar_template(self):
        if self.sidebar_template == None:
            sidebar_template=self.get_url_prefix()+"/sidebar.html"
        else:
            sidebar_template=self.sidebar_template
        return sidebar_template
    
    
    def get_nav_template(self):
        if self.nav_template == None:
            nav_template=self.get_url_prefix()+"/"+self.menu+"_nav.html"
        else:
            nav_template=self.nav_template
        return nav_template
            
    def get_breadcrumb_template(self):
        if self.breadcrumb_template == None:
            breadcrumb_template=self.get_url_prefix()+"/"+self.menu+"_breadcrumb.html"
        else:
            breadcrumb_template=self.breadcrumb_template
        return breadcrumb_template

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["can_create"]=self.can_create
        context["can_update"]=self.can_update
        context["can_delete"]=self.can_delete
        context["can_filter"]=self.can_filter
        context["can_export"]=self.can_export
        context["title"]=self.get_title()
        context["menu"]=self.menu
        context["nav_active"]=self.get_nav_active()
        context["nav_template"]=self.get_nav_template()
        context["breadcrumb_template"]=self.get_breadcrumb_template()
        context["sidebar_template"]=self.get_sidebar_template()
        return context



class admin_Mixin(UserMixin,UserPassesTestMixin):
    
    login_url = "/login/"
    menu="admin"
    breadcrumb_template="admin/breadcrumb.html"
    nav_template="admin/nav.html"
    can_create=True
    can_update=True
    can_delete=True
    can_filter=True
    

    def test_func(self):
        if hasattr(self.request.user,'administratif') or hasattr(self.request.user,'enseignant'):
            output=True
        else:
            output=False
        return output

    def get_url_prefix(self):
        if "admin_ens" in self.request.path:
            url_prefix="admin_ens"
        if "admin_adm" in self.request.path:
            url_prefix="admin_adm"
        return url_prefix



class ETUMixin(UserMixin,UserPassesTestMixin):
    
    login_url = "/login/"
    url_prefix="admin_etu"

    def test_func(self):
        if hasattr(self.request.user, 'etudiant'):
            output=True
        else:
            output=False
        return output
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["is_etu"]=True
        return context



class ENSMixin(UserMixin,UserPassesTestMixin):

    login_url = "/login/"
    url_prefix="admin_ens"
    can_create=False
    can_update=True
    can_delete=False

    
    def test_func(self):
        if hasattr(self.request.user,'enseignant'):
            output=True
        else:
            output=False
        return output
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["is_ens"]=True
        return context

class RafMixin(UserMixin,UserPassesTestMixin):
    
    login_url = "/login/"
    url_prefix="admin_raf"
    menu=None
    can_create=True
    can_update=True
    can_delete=True
    
    def test_func(self):
        output=False
        formation=None
        if "formation" in self.kwargs:
            formation=get_object_or_404(Formation,pk=self.kwargs["formation"])
        if "promotion" in self.kwargs:
            promotion=get_object_or_404(Promotion,pk=self.kwargs["promotion"])
            formation=promotion.formation

        if hasattr(self.request.user, 'enseignant'):
            if self.request.user.enseignant==formation.responsable:
                output=True
        
        return output
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["is_raf"]=True
        return context

class ADMMixin(UserMixin,UserPassesTestMixin):
    
    login_url = "/login/"
    url_prefix="admin_adm"
    
    def test_func(self):
        if hasattr(self.request.user,'administratif'):
            output=True
        else:
            output=False
        return output

class TUTMixin(UserMixin,UserPassesTestMixin):
    
    login_url = "/login/"
    url_prefix="admin_tut"
    
    def test_func(self):
        if hasattr(self.request.user,'tuteur_entreprise'):
            output=True
        else:
            output=False
        return output


# View

class AdminListView(generic.ListView):
    
    title=None
    subtitle=None
    is_markdown=False
    list_template=None
    form=None

    def get_template_names(self):
        if self.template_name==None:
            template_name="list.html"
        else:
            template_name=self.template_name
        return template_name
    
    def get_list_template(self):
        if self.list_template == None:
            if hasattr(self.object_list,"model"):
                opts = self.object_list.model._meta
                list_template="%s/%s_list.html" % (opts.app_label, opts.model_name)
        else:
            list_template=self.list_template
        return list_template
    
    def get_title(self):
        if self.title == None:
            title="Liste %s" % self.model.__name__.replace("_"," ")
        else:
            title=self.title
        return title
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context["subtitle"]=self.subtitle
        context["is_markdown"]=self.is_markdown
        context["list_template"]=self.get_list_template()
        if self.form is not None:
            context["form"]=self.form
        return context


class AdminDetailView(generic.DetailView):
    
    title=None
    subtitle=None
    is_markdown=False
    detail_template=None

    def get_title(self):
        if self.title == None:
            title="Detail %s" % self.model.__name__
        else:
            title=self.title
        return title

    def get_template_names(self):
        if self.template_name==None:
            template_name="detail.html" 
        else:
            template_name=self.template_name
        return template_name
    
    def get_detail_template(self):
        if self.detail_template == None:
            opts = self.object._meta
            detail_template="%s/%s_detail.html" % (opts.app_label, opts.model_name)
        else:
            detail_template=self.detail_template
        return detail_template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subtitle"]=self.subtitle
        context["is_markdown"]=self.is_markdown
        context["detail_template"]=self.get_detail_template()
        return context

class AdminCreateView(generic.CreateView):
    
    title=None
    subtitle=None
    is_markdown=False
    
    def get_title(self):
        if self.title == None:
            title="Creation %s" % self.model.__name__
        else:
            title=self.title
        return title

    def get_template_names(self):
        if self.template_name==None:
            template_name="%s/form.html" %self.base_template_name
        else:
            template_name=self.template_name
        return template_name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subtitle"]=self.subtitle
        context["is_markdown"]=self.is_markdown
        return context

    def get_success_url(self, **kwargs):
        model_name=self.model.__name__
        if "pk" in self.kwargs:
            del self.kwargs["pk"]
        return reverse_lazy('%s_%s_list' % (self.base_template_name,model_name.lower()) , kwargs = self.kwargs)


class AdminUpdateView(generic.UpdateView):
    
    title=None
    subtitle=None
    is_markdown=False
    
    def get_template_names(self):
        if self.template_name==None:
            template_name="%s/form.html" %self.base_template_name
        else:
            template_name=self.template_name
        return template_name

    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context["subtitle"]=self.subtitle
        context["is_markdown"]=self.is_markdown
        return context
    
    def get_success_url(self, **kwargs):
        model_name=self.model.__name__
        return reverse_lazy('%s_%s_detail' % (self.base_template_name,model_name.lower()) , kwargs = self.kwargs)


class AdminFormView(generic.FormView):
    
    title=None
    subtitle=None
    is_markdown=False
    success_url="../../"
    
    
    def get_template_names(self):
        if self.template_name==None:
            template_name="form.html"
        else:
            template_name=self.template_name
        return template_name
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subtitle"]=self.subtitle
        context["is_markdown"]=self.is_markdown
        return context
    


class AdminDeleteView(generic.DeleteView):
    
    base_template_name=None
    menu=None
    submenu=None
    title=None
    subtitle=None

    def get_template_names(self):
        if self.template_name==None:
            template_name="%s/delete.html" %self.base_template_name
        else:
            template_name=self.template_name
        return template_name

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context["subtitle"]=self.subtitle
        return context

    def get_success_url(self, **kwargs):
        model_name=self.model.__name__
        del self.kwargs["pk"]
        return reverse_lazy('%s_%s_list' % (self.base_template_name,model_name.lower()) , kwargs = self.kwargs)

#################### AJAX ####################

class AjaxableDetailMixin(generic.DetailView):
    
    html_id=None
    
    def get_template_name(self):
        if self.template_name:
            template_name=self.template_name
        else:
            model_name=self.model.__name__
            template_name="%s/%s_detail.html" %(self.url_prefix,model_name.lower())
        return template_name
    
    def get_html_id(self):
        if self.html_id:
            html_id=self.html_id
        else:
            model_name=self.model.__name__
            html_id="%s_detail" % model_name.lower()
        return html_id

    def render_to_response(self, context, **response_kwargs):
        html=render_to_string(self.get_template_name(),context=context,request=self.request,)
        html_id=self.get_html_id()
        title="Detail %s" % self.object
        return JsonResponse({"title":title,"id":html_id,"content":html})


class AjaxableCreateMixin(generic.CreateView):
    
    template_name="bootstrap_form.html"
    success_url ="./"
    
    def get(self, request, *args, **kwargs):
        form=self.get_form()
        class_name=self.model.__name__
        form_html=render_to_string(self.template_name, {"form":form,"class_name":class_name},request=self.request,)
        modal_title="Creation %s" % class_name
        return JsonResponse({"title":modal_title,"id":"form","content":form_html})
    
    def get_invalid_json(self,form):
        dict={}
        dict["content"]=render_to_string(self.template_name, {"form":form},request=self.request,)
        return dict
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        json=self.get_invalid_json(form)
        return JsonResponse(json, status=400)

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {'pk': self.object.pk,}
            return JsonResponse(data)
        else:
            return response


class AjaxableUpdateMixin(generic.UpdateView):
    
    template_name="bootstrap_form.html"
    success_url ="./"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form=self.get_form()
        form_html=render_to_string(self.template_name, {"form":form},request=self.request,)
        modal_title="Modification %s" % self.object
        return JsonResponse({"title":modal_title,"id":"form","content":form_html})
    
    def get_invalid_json(self,form):
        dict={}
        dict["form"]=render_to_string(self.template_name, {"form":form},request=self.request,)
        return dict
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        json=self.get_invalid_json(form)
        return JsonResponse(json, status=400)

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {'pk': self.object.pk,}
            return JsonResponse(data)
        else:
            return response

class AjaxableFormMixin(generic.FormView):
    
    template_name="bootstrap_form.html"
    success_url ="./"

    def process_form(self,form):
        return form
    
    def get(self, request, *args, **kwargs):
        form=self.get_form()
        form_html=render_to_string(self.template_name, {"form":form},request=self.request,)
        modal_title="Formulaire Création"
        return JsonResponse({"title":modal_title,"id":"form","content":form_html})
    
    def get_invalid_json(self,form):
        dict={}
        dict["form"]=render_to_string(self.template_name, {"form":form},request=self.request,)
        return dict
    
    def form_valid(self, form):
        self.process_form(form)
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {'status': 'ok',}
            return JsonResponse(data)
        else:
            return response
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        json=self.get_invalid_json(form)
        return JsonResponse(json, status=400)


class AjaxableDeleteMixin(generic.DeleteView):
    
    template_name="bootstrap_form_delete.html"
    success_url ="./"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_html=render_to_string(self.template_name, {"object":self.object},request=self.request,)
        modal_title="Suppression %s" % self.object
        return JsonResponse({"title":modal_title,"id":"form","content":form_html})

    def delete(self, request, *args, **kwargs):

        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()

        if self.request.is_ajax():
            data = {'pk': self.object.pk,}
            return JsonResponse(data)
        else:
            return HttpResponseRedirect(success_url)



