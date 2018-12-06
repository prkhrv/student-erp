from .models import student
from django import forms

class studentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ('name','gender',
                    'roll','dob','email','phone',
                    'branch','address','year')
