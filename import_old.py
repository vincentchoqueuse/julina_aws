import sqlite3
import sys,os
import django
sys.path.append(os.getcwd())

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "julina.settings")
django.setup()

from formations.models import *
from promotions.models import *
from entreprises.models import *

Contrat.objects.filter(affectation__promotion__annee=2017).delete()


print("Opened database successfully");






