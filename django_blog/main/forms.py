
from django import forms


class CreatePost(forms.Form):
    Title = forms.CharField(max_length=200)
    Description = forms.CharField(max_length=500)
    Body = forms.CharField(widget=forms.Textarea(), max_length=10000)
