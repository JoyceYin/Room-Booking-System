from django import forms
from . import models
from detail.models import room_info
from search.models import listing

class SubmitForm(forms.Form):
	name = forms.CharField(label='Room Name', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
	type = forms.CharField(label='Room Type', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
	street = forms.CharField(label='Location', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	bathrooms = forms.CharField(label='Bathrooms', max_length = 5, widget=forms.TextInput(attrs={'class': 'form-control'}))
	bedrooms = forms.CharField(label='Bedrooms', max_length = 5, widget=forms.TextInput(attrs={'class': 'form-control'}))
	amenities = forms.CharField(label='amenities', max_length = 200, widget=forms.TextInput(attrs={'class': 'form-control'}))
	accommodates = forms.CharField(label='Accommodates', max_length=5, widget=forms.TextInput(attrs={'class': 'form-control'}))
	price = forms.CharField(label='Price', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
	image_url = forms.CharField(label='Picture Link', max_length = 1000, widget=forms.TextInput(attrs={'class': 'form-control'}))
	description = forms.CharField(label='Describe your Room', max_length = 10000, widget=forms.TextInput(attrs={'class': 'form-control'}))


	class Meta:
		model1 = room_info
		model2 = listing
		fields = ['name', 'type', 'accommodates','bathrooms','bedrooms',
		          'amenities','price','image_url','street','description']
		

	def __init__(self, *args, **kwargs):
		super(SubmitForm, self).__init__(*args, *kwargs)
		self.fields['name'].label = 'Room Name'
		self.fields['type'].label = 'Room Type'
		self.fields['accommodates'].label = 'Accommodates'
		self.fields['bathrooms'].label = 'Bathrooms'
		self.fields['bedrooms'].label = 'Bedrooms'
		self.fields['amenities'].label = 'Amenities'
		self.fields['price'].label = 'Price'
		self.fields['image_url'].label = 'Picture Link'
		self.fields['street'].label = 'Location'
		self.fields['description'].label = 'Describe your Room'
		
	
	def save(self, *args, **kwargs):
		room_info = super(SubmitForm, self).save(commit=False)
		listing = super(SubmitForm, self).save(commit=False)
		#user.email = self.cleaned_data['email']
		room_info.save()
		listing.save()
		return room_info, listing

#	def clean_password(self):
#		password = self.cleaned_data.get('password')
#		if len(password) < 8:
#			raise forms.ValidationError('Password too short')
#		return super(RegisterForm, self).clean_password()
