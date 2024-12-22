from django import forms
from .models import ChaiVaraity, CustomerOrder

class ChaiVarityForm(forms.Form):
    chai_varity = forms.ModelChoiceField(queryset=ChaiVaraity.objects.all(), label="Select chai variety")

class CustomerOrderForm(forms.ModelForm):
    class Meta:
        model = CustomerOrder
        fields = [
            'name', 'number', 'location', 'tea_name', 'tea_price', 
            'quantity', 'price', 'total_price', 'additional_tea'
        ]
        widgets = {
            'additional_tea': forms.HiddenInput()  # Hide additional tea JSON field
        }
