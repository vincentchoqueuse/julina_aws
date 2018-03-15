from django import template
from django.core.urlresolvers import reverse, reverse_lazy
from formations.models import Formation
from promotions.models import Promotion
from entreprises.models import Entreprise,Contrat
from django.db.models import Max,Count

register = template.Library()



def formations_as_list(entreprise):
    formations_pk=Contrat.objects.filter(entreprise=entreprise).values_list("affectation__promotion__formation", flat=True).distinct()
    formations=Formation.objects.filter(pk__in=formations_pk)
    list_formations_string = [str(formation) for formation in formations]
    return ", ".join(list_formations_string)

def promotions_as_list(entreprise):
    promotions_pk=Contrat.objects.filter(entreprise=entreprise).values_list("affectation__promotion", flat=True).distinct()
    promotions=Promotion.objects.filter(pk__in=promotions_pk)
    list_promotions_string = [str(promotion) for promotion in promotions]
    return ", ".join(list_promotions_string)

def url_replace(request, field, value):
    dict = request.GET.copy()
    dict[field] = value
    return dict.urlencode()



register.filter('formations_as_list',formations_as_list)
register.filter('promotions_as_list',promotions_as_list)
register.filter('url_replace',url_replace)
