from django import forms
from app.models import *

class Student(forms.Form):
    name=forms.CharField(max_length=200)
    age=forms.IntegerField()



class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields='__all__'