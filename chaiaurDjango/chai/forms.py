from django import forms
from .models import ChaiVaraity, CustomerOrder,Review,Video

class ChaiVarityForm(forms.Form):
    chai_varity = forms.ModelChoiceField(queryset=ChaiVaraity.objects.all(), label="Select chai variety")

class CustomerOrderForm(forms.ModelForm):
    class Meta:
        model = CustomerOrder
        fields = [
            'name', 'number', 'quantity',
        ]

        
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'rating', 'review']
        widgets = {
            'rating': forms.RadioSelect(choices=[(i, f'{i} Star{"s" if i > 1 else ""}') for i in range(1, 6)]),
            'review': forms.Textarea(attrs={'rows': 3}),
        }
        
class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'video_file']
