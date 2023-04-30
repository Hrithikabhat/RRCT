from socket import fromshare
from django import forms
from .models import k,patient

class pf(forms.ModelForm):
    class meta:
        model= patient
        fields="__all__"
        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields['kind'].queryset=k.objects.none()