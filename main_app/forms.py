from django import forms
from .models import Item

class Item_Form(forms.ModelForm):
  class Meta:
    model = Item
    fields = ['description']