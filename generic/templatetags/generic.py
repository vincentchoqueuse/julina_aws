from django import template
import markdown
from django.db import models
from promotions.models import Affectation_Etudiant, Bulletin
from django.utils.safestring import mark_safe
from django.db.models import Avg
import os
from django.http import QueryDict


register = template.Library()

@register.simple_tag
def query_transform(request, page):
    dict_ = request.GET.copy()
    dict_["page"] = page
    return dict_.urlencode()

@register.simple_tag
def test_url_active(request, menu,value):
    test_string="{}/{}/".format(menu,value)
    if test_string in request.path:
        output="active"
    else:
        output=""
    return output



def find_note(bulletin, module_pk):
    
    note=Note.objects.filter(bulletin=bulletin,module__pk=module_pk)
    
    if note.exists():
        output=note[0].moyenne
    else:
        output="Indéterminé"
    
    return output

def find_nb_etu(parcours, promotion_pk):
    
    affectations=Affectation_Etudiant.objects.filter(parcours=parcours,promotion__pk=promotion_pk)
    nb_etu=affectations.count()
    return nb_etu

def find_moy(parcours, promotion_pk):
 
    bulletin=Bulletin.objects.filter(affectation__parcours=parcours,affectation__promotion__pk=promotion_pk)
    result=bulletin.aggregate(Avg('moyenne'))
    moyenne=result["moyenne__avg"]
    if isinstance(moyenne,float):
        moyenne=round(moyenne,2)
    
    return moyenne

def as_p(object):
    
    html=""
    
    for field in object._meta.get_fields():

        if not (isinstance(field,models.ManyToManyRel)) and not (isinstance(field,models.OneToOneRel)) and not (isinstance(field,models.ManyToOneRel)):
        
            if field.name is not "id":
            
                value=getattr(object,field.name)
                html=html+"<div><label>"+str(field.verbose_name)+"</label>"
                html=html+"<p class='field_value'>"+markdown.markdown(str(value))+"</p></div>"


    return mark_safe(html)


def as_description(object,list_display):

    html="<dl class='row'>"
    
    for fieldname in list_display:
        fieldvalue=getattr(object,fieldname)
        html=html+"<dt class='col-sm-3'>"+str(fieldname)+"</dt>"
        html=html+"<dd class='col-sm-9'>"+str(fieldvalue)+"</dd>"
        
    html=html+"</dl>"
    
    return mark_safe(html)

def as_markdown_description(object,list_display):
    
    html="<dl class='row'>"
    
    for fieldname in list_display:
        fieldvalue=getattr(object,fieldname)
        html=html+"<dt class='col-sm-3'>"+str(fieldname)+"</dt>"
        html=html+"<dd class='col-sm-9'>"+markdown.markdown(str(fieldvalue))+"</dd>"
    
    html=html+"</dl>"
    
    return mark_safe(html)


def as_markdown(object):
    if object is None:
        html=""
    else:
        html=markdown.markdown(object)
    return mark_safe(html)

def file_extension(object):
    name, extension = os.path.splitext(object.url)
    return extension

def as_row(object,list_display):
    

    #first column
    fieldvalue=getattr(object,list_display[0])
    if callable(fieldvalue):
        fieldvalue=fieldvalue()

    html="<tr><td class='first_column'><a href='./"+str(object.pk)+"/'>"+str(fieldvalue)+"</a></td>"
    
    # other columns
    for fieldname in list_display[1:]:
        
        fieldvalue=getattr(object,fieldname)
        
        if callable(fieldvalue):
            fieldvalue=str(fieldvalue())
        else:
            field=object._meta.get_field(fieldname)
            
            if isinstance(field,models.EmailField):
                fieldvalue="<a class='btn btn-default btn-sm' href='mailto:"+str(fieldvalue)+"'><i class='fa fa-envelope' aria-hidden='true'></i></a>"
            
            if isinstance(field,models.DateTimeField):
                fieldvalue=fieldvalue.strftime("%Y-%m-%d %H:%M:%S")
            
            if isinstance(field,models.BooleanField):
                if fieldvalue==True:
                    fieldvalue="<i class='fa fa-check' aria-hidden='true'></i>"
                else:
                    fieldvalue="<i class='fa fa-close' aria-hidden='true'></i>"
        
            if isinstance(field,models.CharField):
                fieldvalue=str(fieldvalue)
                fieldvalue=(fieldvalue[:40] + '...') if len(fieldvalue) > 40 else fieldvalue

            if isinstance(field,models.FloatField):
                fieldvalue=str(fieldvalue)

            if isinstance(field,models.IntegerField):
                fieldvalue="%d" % fieldvalue
    
    
        html=html+"<td>"+str(fieldvalue)+"</td>"
        
    return mark_safe(html)

def as_progress_bar(object):
    try:
        value=int(object)
        class_name=["danger","warning","info","info","success"]
        value_100=(value+1)*20

        html="<div class='progress'>"
        html=html+"<div class='progress-bar bg-%s' role='progressbar' style='width: %d%%' aria-valuenow='%d' aria-valuemin='0' aria-valuemax='100'></div>" %(class_name[value],value_100,value_100)
        html=html+"</div>"
    except:
        html="None"
    return mark_safe(html)

def as_table(object_list,list_display):

    action=list_display[-1]

    html=""

    for object in object_list:
        
        #first column
        fieldvalue=getattr(object,list_display[0])
        if callable(fieldvalue):
            fieldvalue=fieldvalue()
        
        html=html+"<tr><td class='first_column'><a href='./"+str(object.pk)+"/'>"+str(fieldvalue)+"</a></td>"
    
        # other columns
        for fieldname in list_display[1:-1]:
    
            fieldvalue=getattr(object,fieldname)
            
            if callable(fieldvalue):
                fieldvalue=fieldvalue()
            else:
                field=object._meta.get_field(fieldname)
            
                if isinstance(field,models.EmailField):
                    fieldvalue="<a class='btn btn-default btn-sm' href='mailto:"+str(fieldvalue)+"'><i class='fa fa-envelope' aria-hidden='true'></i></a>"
                
                if isinstance(field,models.DateTimeField):
                    fieldvalue=fieldvalue.strftime("%Y-%m-%d %H:%M:%S")

                if isinstance(field,models.BooleanField):
                    if fieldvalue==True:
                        fieldvalue="<i class='fa fa-check' aria-hidden='true'></i>"
                    else:
                        fieldvalue="<i class='fa fa-close' aria-hidden='true'></i>"

                if isinstance(field,models.CharField):
                    fieldvalue=str(fieldvalue)
                    fieldvalue=(fieldvalue[:40] + '...') if len(fieldvalue) > 40 else fieldvalue
                        
                if isinstance(field,models.FloatField) or isinstance(field,models.IntegerField):
                    fieldvalue=str(fieldvalue)
    
        
            html=html+"<td>"+fieldvalue+"</td>"
    
    

        if action == "D":
            html=html+"<td><a href='./"+str(object.pk)+"/delete' class='btn btn-default btn-sm'><i class='fa fa-trash' aria-hidden='true'></i></a></td>"
    
        html=html+"</tr>"
        

    return mark_safe(html)


register.filter('as_markdown_description', as_markdown_description)
register.filter('as_description', as_description)
register.filter('as_table', as_table)
register.filter('as_row', as_row)
register.filter('as_markdown', as_markdown)
register.filter('as_progress_bar', as_progress_bar)
register.filter('file_extension', file_extension)
register.filter('find_note', find_note)
register.filter('find_nb_etu', find_nb_etu)
register.filter('find_moy', find_moy)

