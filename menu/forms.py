from django import forms
from .models import Dish


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ("name", "description", "price", "category", "is_available")

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "is_available": forms.CheckboxInput(attrs={"class": "form-control-input"}),
        }
