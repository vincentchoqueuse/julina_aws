from django import template
from django.core.urlresolvers import reverse, reverse_lazy
from formations.models import UE

register = template.Library()

def as_html(bulletin):

    bulletin_list=[]
    parcours=bulletin.affectation.parcours
    
    string="<table class='table'>"
    
    if parcours:
        for ue in UE.objects.filter(module__parcours=parcours).distinct():
            notes_list=[]
            string=string+"<tr><th>UE"+str(ue.numero)+"</th><th>"+ue.intitule+"</th><th></th></tr>"
            for module in parcours.modules.all().filter(ue=ue):
                note=bulletin.note_set.filter(module=module)
                if len(note)==0:
                    note_value=0
                else:
                    note_value=note[0].moyenne
                url=str(reverse_lazy('modules_detail', kwargs = {'pk': module.pk}))
                string=string+"<tr><td><a href="+url+">"+module.code_scodoc+"</a></td><td>"+module.intitule+"</td><td>"+str(note_value)+"</td></tr>"

    string=string+"</table>"
    return string


register.filter('as_html',as_html)
