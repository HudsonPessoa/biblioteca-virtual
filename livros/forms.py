from django import forms
from .models import Livro


class LivroForm(forms.ModelForm):

    class Meta:
        model = Livro
        fields = '__all__'

        widgets = {

            'titulo': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),

            'ano_publicacao': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'quantidade': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'autor': forms.Select(attrs={
                'class': 'form-select'
            }),

            'categoria': forms.Select(attrs={
                'class': 'form-select'
            }),
        }