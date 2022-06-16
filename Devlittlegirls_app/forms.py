from django import forms
from site_devlittlegirls_app.models import Site

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = '__all__'