from django import forms
from . models import Products
class product_form(forms.ModelForm):
    class Meta:
        model=Products
        fields=['name','description','price','image']