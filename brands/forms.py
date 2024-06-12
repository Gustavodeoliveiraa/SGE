from .models import Brand
from django import forms


class BrandForm(forms.ModelForm):

    class Meta:
        model = Brand
        fields = ['name', 'description']  # type: ignore
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            )
        }
        labels = {
            'name': 'Nome', 'description': 'Descrição',
        }