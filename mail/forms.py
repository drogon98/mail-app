from django import forms

from .models import Mail,Search

class MailForm(forms.ModelForm):
	class Meta:
		model=Mail
		fields=["sender","subject","message","to"]

class SearchForm(forms.ModelForm):
	class Meta:
		model=Search
		fields="__all__"