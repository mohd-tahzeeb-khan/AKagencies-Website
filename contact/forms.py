from django.forms import ModelForm
from django import forms


class formcontactus(forms.Form):
    email=forms.EmailField(label="Email Id", required=True)
    mobileno=forms.IntegerField(label="Mobile No", required=True)
    name=forms.CharField(label="Name", required=True)
    description=forms.CharField( widget=forms.Textarea )