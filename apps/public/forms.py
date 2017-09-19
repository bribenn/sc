from django import forms

class DemoForm(forms.Form):
	name = forms.CharField(required=True)
	company = forms.CharField()
	from_email = forms.EmailField(required=True)
	phone = forms.IntegerField(required=True)
	interest = forms.CharField(widget=forms.Textarea)
			