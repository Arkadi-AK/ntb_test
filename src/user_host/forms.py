from django import forms

from .models import Host


class HostForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = ['ip_address', 'port', 'type_of_resource']
        widgets = {'author': forms.HiddenInput()}
