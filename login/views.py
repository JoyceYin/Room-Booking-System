from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
#import datetime
from .form import LoginForm, RegisterForm
from search.models import host_info
from center.models import user_id
from .models import users
import random

# Create your views here.


def login(request):
	if request.method == "POST":
		username = ''
		passwd = ''
		message = ''
		form = LoginForm(request.POST or None)

		if form.is_valid():
			username = form.cleaned_data.get("username")
			passwd = form.cleaned_data.get("password")
			usertype = form.cleaned_data.get("usertype")
			type = request.GET.get('users.usertype')

			try:
				if usertype == '1':
					userinfo = user_id.objects.get(name=username)

					if userinfo.password == passwd:
						request.session['is_login'] = True
						request.session['username'] = userinfo.name
						request.session['bookid'] = userinfo.UID
						#request.session['booker'] = userinfo.usertype
						request.session['type'] = 1
						if request.session.get('is_login', None):

							return HttpResponseRedirect("/index/")

				elif usertype == '2':
					userinfo = host_info.objects.get(name=username)

					if userinfo.password == passwd:
						request.session['is_login'] = True
						request.session['username'] = userinfo.name
						request.session['hostid'] = userinfo.HID
						#request.session['host'] = userinfo.usertype
						request.session['type'] = 2
						if request.session.get('is_login', None):

							return HttpResponseRedirect("/index/")

				else:
					message = 'Incorrect Password!'
			except:
				message = 'User not exist!'
			return render(request, 'login.html', {'form': form, 'message': message, "title": "Log in"})
	else:
		form = LoginForm()
	return render(request, 'login.html', {'form': form, "title": "Log in", "type":"type"})



def register(request):
	#if request.session.get('is_login', None):
		#return HttpResponseRedirect("/index/")
	if request.method == "POST":
		username=' '
		password = ' '
		password2 = ' '
		email =''
		about = ''
		message = ' '
		form = RegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			password2 = form.cleaned_data["password2"]
			email = form.cleaned_data["email"]
			usertype = form.cleaned_data["usertype"]

			if password != password2: 
				message = " password inconsistence "
				return render(request, 'register.html', {'form': form, 'message': message, "title": "Sign Up"})
			
			else:
				same_name_user = users.objects.filter(username=username)
				if same_name_user:
					message = 'username already exist! '
					return render(request, 'register.html', {'form': form, 'message': message, "title": "Sign Up"})
				
				same_email_user = users.objects.filter(email=email)
				if same_email_user:
					message = 'Email address alreay exist! '
					return render(request, 'register.html', {'form': form, 'message': message, "title": "Sign Up"})
                # if everything okay
                #users.objects.create()
				
				if usertype == '1':
					new_user = user_id()
					new_user.name = username
					new_user.password = password
					new_user.email = email
					new_user.UID = random.randint(1,500000)
					new_user.save()

					new_user1 = users()
					new_user1.username = username
					new_user1.password = password
					new_user1.email = email
					new_user1.save()
					#new_user1 = users()
					#new_user = new_user1
					
				if usertype == '2':
					new_user = host_info()
					new_user.name = username
					new_user.password = password
					new_user.email = email
					new_user.HID = random.randint(500000,1000000)
					new_user.save()

					new_user1 = users()
					new_user1.username = username
					new_user1.password = password
					new_user1.email = email
					new_user1.save()

				return redirect("/login/")# change to login page
			#message = 'No'
			#return render(request, 'register.html', {'form': form, 'message': message, "title": "Sign Up"})

	form = RegisterForm()
	return render(request, 'register.html', {'form': form, "title": "Sign Up"})




def logout(request):
	if not request.session.get('is_login', None):
		return redirect("/index/")

	request.session.flush()
	return redirect("/index/")