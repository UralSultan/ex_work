from django import forms
from django.forms import widgets


class GuestSearchForm(forms.Form):
    name = forms.CharField(
        label="Имя гостя",
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={
            "placeholder": "Введите имя гостя",
        }),
    )

class GuestBookAddForm(forms.Form):
    author_name = forms.CharField(max_length=50, required=True, label="Имя гостя")
    author_email = forms.EmailField(required=True, label="Почта")
    content = forms.CharField(max_length=500, required=True, widget=widgets.Textarea, label="Текст")