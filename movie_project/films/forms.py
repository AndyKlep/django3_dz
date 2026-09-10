from django import forms
from .models import Film


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = (
            'title',
            'description',
            'review',
        )

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Например, Интерстеллар',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 5,
                    'placeholder': 'Кратко опишите фильм',
                }
            ),
            'review': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 5,
                    'placeholder': 'Напишите ваш отзыв о фильме',
                }
            ),
        }

        labels = {
            'title': 'Название фильма',
            'description': 'Описание фильма',
            'review': 'Ваш отзыв',
        }