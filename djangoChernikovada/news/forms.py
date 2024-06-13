from .models import Articles, Comment
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, ImageField
from django import forms


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}),
            'anons': TextInput(attrs={'class': 'form-control', 'placeholder': 'Анонс'}),
            'full_text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Содержание'}),
            'date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата'}),
        }


