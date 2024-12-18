from django import forms
from .models import ChaiVaraity


class ChaiVarityForm(forms.Form):
    chai_varity = forms.ModelChoiceField(queryset=ChaiVaraity.objects.all(),label="select chai variety") 