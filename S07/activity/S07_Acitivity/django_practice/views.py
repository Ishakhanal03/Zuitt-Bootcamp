from django.shortcuts import render,redirect

from django.http import HttpResponse
from .models import GroceryItem
from django.forms.models import model_to_dict
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):
	# return HttpResponse("Hello from the views.py file!")
	groceryitem_list = GroceryItem.objects.all()
	context = {
		'groceryitem_list' : groceryitem_list,
		'user': request.user
	}
	return render(request, 'django_practice/index.html', context)

def groceryitem(request, groceryitem_id):
	
	groceryitem = model_to_dict(GroceryItem.objects.get(pk = groceryitem_id))

	return render(request, "django_practice/tobuy.html", groceryitem)

def register(request):
	
	users = User.objects.all()
	is_user_registered = False

	user = User()
	user.username = 'KaveriStha'
	user.first_name = "Kaveri"
	user.last_name = "Shrestha"
	user.email = "kaveri@mail.com"
	user.set_password("kaveri1234") 
	user.is_staff = False
	user.is_active = True

	for indiv_user in users:
		if indiv_user.username == user.username :
			is_user_registered = True
			break

	if is_user_registered == False :
		user.save()

	context = {
		"first_name" : user.first_name,
		"last_name" : user.last_name,
		"is_user_registered" : is_user_registered
	}

	return render(request, 'django_practice/register.html', context)

def change_password(request):
	is_user_authenticated = False
	# in djang0 we have the authenticate() method to check whether the credential is registered on our database or not

	# using the authenticate method if the credentials are correct it will return the object of that specific user otherwise it will return None.
	user = authenticate(username = "KaveriStha", password = "kaveri1234")

	if user is not None:
		authenticated_user = User.objects.get(username = "KaveriStha")

		authenticated_user.set_password("kaveri12")

		authenticated_user.save()

		is_user_authenticated = True

	context = {
		"is_user_authenticated" : is_user_authenticated
	}

	return render(request, "django_practice/changepassword.html", context)	

def login_view(request):
	username = "KaveriStha"
	password = "kaveri12"

	user = authenticate(username = username, password = password)

	is_user_authenticated = False

	if user is not None:
		# save the user's Id in the session using django's session framework.
		login(request, user)
		return redirect("index")
	else:

		context = {
			"is_user_authenticated": is_user_authenticated
		}

		return render(request, "django_practice/login.html", context)

def logout_view(request):
	logout(request)

	return redirect("index")
