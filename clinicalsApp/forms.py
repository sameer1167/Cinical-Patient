from django import forms
from clinicalsApp.models import paitent,clinicaldata


class paitentform(forms.ModelForm):
    class Meta:
        model = paitent
        fields='__all__'

class clinicaldataform(forms.ModelForm):
    class Meta:
        model = clinicaldata
        fields = '__all__'