from django import forms
from . import models


class LoginForm(forms.Form):
	usertype=(
		('1', 'booker'),
		('2', 'host'),
		)
	username = forms.CharField(label = 'Username', max_length=25, widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(label= 'Password', max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	usertype = forms.ChoiceField(label='usertype', choices=usertype)

	class Meta:
		model = models.users
		fields = ['username', 'password','usertype']

	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, *kwargs)
		self.fields['username'].label = 'Username'
		self.fields['password'].label = 'Password'
		self.fields['usertype'].label = 'usertype'




class RegisterForm(forms.Form):
	usertype=(
		('1', 'booker'),
		('2', 'host'),
		)
	username = forms.CharField(label='Username', max_length=25, widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	password2 = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(label='Email', max_length = 40, widget=forms.EmailInput(attrs={'class': 'form-control'}))
	usertype = forms.ChoiceField(label='usertype', choices=usertype)


	class Meta:
		model = models.users
		fields = ['username', 'password', 'password2', 'email', 'usertype','about']

	def __init__(self, *args, **kwargs):
		super(RegisterForm, self).__init__(*args, *kwargs)
		self.fields['username'].label = 'Username'
		self.fields['password'].label = 'Password'
		self.fields['password2'].label = 'password2'
		self.fields['email'].label = 'email'
		self.fields['usertype'].label = 'usertype'
	
	def save(self, *args, **kwargs):
		user = super(RegisterForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.save()
		return user

#	def clean_password(self):
#		password = self.cleaned_data.get('password')
#		if len(password) < 8:
#			raise forms.ValidationError('Password too short')
#		return super(RegisterForm, self).clean_password()