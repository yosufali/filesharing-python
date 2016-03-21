from django import forms

class FileForm(forms.Form):
	file = forms.FileField(label='Select a file :)')
    # name = forms.CharField(max_length=500)
    # file = forms.FileField()
