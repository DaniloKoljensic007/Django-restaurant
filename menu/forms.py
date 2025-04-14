from django import forms
from .models import Dish


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ("name", "description", "price", "category")

        widgets = {
            "name": forms.TextInput(),
            "description": forms.Textarea(),
            "price": forms.NumberInput(),
            "category": forms.Select(),
        }
