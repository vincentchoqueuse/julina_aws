import requests
import csv
import io
from django import forms


def convert_2_float(string):
    if string == "":
        number=0
    else:
        number=float(string)
    return number


class ImportFormation(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    google_sheet_url = forms.URLField(label="Google Spreadsheet ID")

class ImportMixin():
    
    def import_from_spreadheet(self, request, queryset):
        if "do_action" in request.POST:
            form = ImportFormation(request.POST)
            
            if form.is_valid():
                url=form.cleaned_data["google_sheet_url"]
                sheet_id="/".join(url.split('/')[:6])
                sheet_gid=url.split('gid=')[-1]
                url_import="%s/export?format=csv&gid=%s" % (sheet_id,sheet_gid)
                
                #importation de la formation
                headers={}
                headers["User-Agent"]= "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0"
                headers["DNT"]= "1"
                headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
                headers["Accept-Encoding"] = "deflate"
                headers["Accept-Language"]= "en-US,en;q=0.5"
                lines = []
                
                r = requests.get(url_import)
                data = {}
                cols = []
                sio = io.StringIO( r.text, newline=None)
                
                reader = csv.reader(sio, dialect=csv.excel)
                self.process_import(queryset,reader)
                self.message_user(request, "Importation effectuée avec succes")
                return
        else:
            form = ImportFormation(initial={'_selected_action': "import_from_spreadheet"})
        
        return render(request,"admin/formations/importation.html",{'title': u'Selection des parametres','form': form})
    
    import_from_spreadheet.short_description = "Importation Formation GS"
