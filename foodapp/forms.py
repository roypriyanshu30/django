from django import forms
class fooditemform(forms.Form):
    type2=forms.CharField(max_length=200)
    vitaminpresent=forms.CharField(max_length=200)
    name1=forms.CharField(max_length=200)
    
