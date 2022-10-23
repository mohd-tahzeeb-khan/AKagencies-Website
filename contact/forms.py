from django.forms import ModelForm
from django import forms


class formcontactus(forms.Form):
    name=forms.CharField(label="Name", required=True , widget=forms.TextInput(attrs={'style':'width:40rem'}))
    email=forms.EmailField(label="Email Id", required=True, widget=forms.TextInput(attrs={'style':'width:40rem'})) 
    mobileno=forms.IntegerField(label="Mobile No", required=True, widget=forms.TextInput(attrs={'style':'width:40rem'}))
    description=forms.CharField(widget=forms.Textarea(attrs={'rows': 10,'cols': 90}))