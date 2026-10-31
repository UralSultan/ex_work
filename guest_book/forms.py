from django import forms


class GuestSearchForm(forms.Form):
    name = forms.CharField(
        label="Имя гостя",
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={
            "placeholder": "Введите имя гостя",
        }),
    )