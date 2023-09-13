from . import models
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['name', 'stock', 'score', 'category']

        error_messages = {
            'name': {
                'required': 'Please enter your name'
            },
            'stock': {
                'required': 'Please enter the stock'
            },
            'score': {
                'required': 'Please enter the score'
            },
            'category': {
                'required': 'Please enter the category'
            }
        }
        