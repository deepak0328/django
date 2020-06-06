from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import TodoModel,UserModel
from datetime import datetime
from django.http import QueryDict

# Create your views here.
def admin_login_view(request):
	return render(request,"pizza_system/admin-login.html")

def authenticate_admin(request):
	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(username = username,password = password)

	#user exists
	if user is not None:
		login(request,user)
		return redirect('admin-homepage')

	#user not exists
	if user is None:
		messages.add_message(request,messages.ERROR,"invalid credentials")
		return redirect('admin-loginpage')


def admin_home_page_view(request):
	context = {'todos' : TodoModel.objects.all()}
	return render(request,"pizza_system/admin-homepage.html",context)

def logout_admin(request):
	logout(request)
	return redirect('admin-loginpage')

def add_todo(request):
	description = request.POST['todo_description']
	createdDate = datetime.now()
	formatedDate = createdDate.strftime("%c")
	TodoModel(todo_description = description,todo_created_date = formatedDate,todo_modified_date = formatedDate).save()
	return redirect('admin-homepage')

def home_page_view(request):
	return render(request,"pizza_system/homepage.html")

def user_registration(request):
	# registeration_details = request.POST.dict()

	form = request.POST

	username = form.get('username')
	password = form.get('password')


	# username = registeration_details('username')
	# password = registeration_details('password')

	re_entered_password = form.get('re_entered_password')
	email = form.get('email')
	first_name = form.get('first_name')
	last_name = form.get('last_name')
	gender = form.get('gender')
	phone_number = form.get('phone_number')
	dob = form.get('dob')

	# username = request.POST['username']
	# password = request.POST['password']


	# # username = registeration_details('username')
	# # password = registeration_details('password')

	# re_entered_password = request.POST['re_entered_password']
	# email = request.POST['email']
	# first_name = request.POST['first_name']
	# last_name = request.POST['last_name']
	# gender = request.POST['gender']
	# phone_number = request.POST['phone_number']
	# dob = request.POST['dob']

	#user name exists
	if User.objects.filter(username = username).exists():
		messages.add_message(request,messages.ERROR,"Username alredy exists!!")
		return redirect('homepage')

	#valid user name
	User.objects.create_user(username = username,password = password).save()
	last_object = len(User.objects.all())-1
	UserModel(user_id = User.objects.all()[last_object].id, email = email ,first_name = first_name,last_name = last_name,gender = gender,phone_number =phone_number,dob = dob).save()
	messages.add_message(request,messages.ERROR,"User successfully registered.Now proceed with login!!")
	return redirect('homepage')

def user_login_view(request):
	return render(request,"pizza_system/user-login.html")

def authenticate_user(request):
	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(username = username,password = password)

	#user exists
	if user is not None:
		login(request,user)
		return redirect('user-homepage')

	#user not exists
	if user is None:
		messages.add_message(request,messages.ERROR,"invalid credentials")
		return redirect('user-loginpage')

def user_home_page_view(request):
	# context = {'todos' : TodoModel.objects.all()}
	return render(request,"pizza_system/user-homepage.html")
