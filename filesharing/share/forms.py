from django import forms

class UploadedFile(forms.Form):
    name = forms.CharField(max_length=500)
    file = forms.FileField()