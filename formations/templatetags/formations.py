from django import template
import markdown
from django.core.urlresolvers import reverse, reverse_lazy
from formations.models import UE, Module,Parcours,Enseignant

register = template.Library()

def get_sorted_by_ue(object):

    
    if type(object) == type(Parcours()):
        module_pk_list=object.modules.all().values_list("pk", flat=True).distinct()
        ues=UE.objects.filter(module__in=module_pk_list).distinct()
        sorted_object_list=[]
        for ue in ues:
            object_list=object.modules.filter(ue=ue)
            sorted_object_list.append({"ue":ue,"object_list":object_list})
    
    else:
        queryset=object
        module_pk_list=queryset.all().values_list("module", flat=True).distinct()
        ues=UE.objects.filter(module__in=module_pk_list).distinct()
        sorted_object_list=[]
        for ue in ues:
            object_list=queryset.filter(module__ue=ue)
            sorted_object_list.append({"ue":ue,"object_list":object_list})

    return sorted_object_list


register.filter('get_sorted_by_ue', get_sorted_by_ue)
