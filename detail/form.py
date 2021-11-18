from django import forms
from center import models


class BookForm(forms.Form):
	indate = forms.DateTimeField()

	class Meta:
		model = models.book
		fields = ['indate']

	def __init__(self, *args, **kwargs):
		super(BookForm, self).__init__(*args, *kwargs)
		self.fields['indate'].label = 'indate'