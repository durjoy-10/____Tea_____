from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'rating', 'review']
        widgets = {
            'rating': forms.RadioSelect(choices=[(i, f'{i} Star{"s" if i > 1 else ""}') for i in range(1, 6)]),
            'review': forms.Textarea(attrs={'rows': 3}),
        }
