from django import forms
from .models import *


class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        # fields = ['first_name', 'last_name', 'phone', 'category',]
        fields = '__all__'
        exclude = ('created_at','slug','user',)