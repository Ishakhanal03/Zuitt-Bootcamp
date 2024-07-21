from django.shortcuts import render, redirect, get_object_or_404

# The from keyword allows importing of necessary classes, methods and other items needed in our application from the "django.http" package wile import keyword defines what are we importing from the package.
# Where in the HttpResponse module will allow us to send response to our user/client
from django.http import HttpResponse

# Import the ToDoItem model
from .models import ToDoItem

# Importing the pre-created user Model
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

from django.forms.models import model_to_dict

from .forms import LoginForm, AddTaskForm, UpdateTaskForm,RegisterForm

from django.utils import timezone

# Create your views here.

def index(request):
	# The all() will get all the objects in the ToDoItem model
	todoitem_list = ToDoItem.objects.filter(user_id = request.user.id)

	output = ', '.join([todoitem.task_name for todoitem in todoitem_list])

	context = {
		'todoitem_list': todoitem_list,
		'user': request.user
	}	

	return render(request, "todolist/index.html", context)

def todoitem(request, todoitem_id):
	#The mode_to_dict() method allows to convert models into dictionaries
	#the get method model method allows to retrieve a specific record using its primary key 
	todoitem = get_object_or_404(ToDoItem, pk = todoitem_id)

	return render(request, "todolist/todoitem.html", model_to_dict(todoitem))


def register(request):	
    users = User.objects.all()
    is_user_registered = False
    context={
        # 'error':False
    }
    if (request.method == "POST"):
        form=RegisterForm(request.POST)
        if form.is_valid()== False:
            form=RegisterForm()
        else:
            print("valid form")
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            confirm_password=form.cleaned_data['confirm_password']
            user=User()
            user.username=username
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            if(password!=confirm_password):
                context={
                    'error':True,
                }
            else:
                print("set password",password)
                user.set_password(password)
            user.is_staff=False
            user.is_active=True
            for indiv_user in users:
                if indiv_user.username==user.username:
                    is_user_registered = True
                    context={
                    'error':True,
                    }
            print(context['error'])
            if is_user_registered == False and context['error']!=True:
                print("saved")
                user.save()
                return redirect ("todolist:login")
    return render(request,'todolist/register.html',context)


# this function will let us change the password of our user

def change_password(request):
	is_user_authenticated = False
	# in djang0 we have the authenticate() method to check whether the credential is registered on our database or not

	# using the authenticate method if the credentials are correct it will return the object of that specific user otherwise it will return None.
	user = authenticate(username = "kaveristha", password = "kaveri1234")

	if user is not None:
		authenticated_user = User.objects.get(username = "kaveristha")

		authenticated_user.set_password("kaveri123")

		authenticated_user.save()

		is_user_authenticated = True

	context = {
		"is_user_authenticated" : is_user_authenticated
	}

	return render(request, "todolist/changepassword.html", context)	

def login_view(request):
	context = {}

	if request.method == "POST":
		form = LoginForm(request.POST)

		if form.is_valid() == False:
			form = LoginForm()

		else:
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			context = {
				"username" :username,
				"password" : password
			}

			user = authenticate(username = username, password = password)

			if user is not None:
				login(request, user)
				return redirect('todolist:index')

			else:
				context = {
					"error" : True
				}

	return render(request, "todolist/login.html", context)



def logout_view(request):
	logout(request)

	return redirect("todolist:index")

def add_task(request):
	context = {}

	if request.method == "POST":
		form = AddTaskForm(request.POST)

		if form.is_valid() == False:
			form = AddTaskForm()

		else:
			task_name = form.cleaned_data['task_name']
			description = form.cleaned_data['description']

			duplicates = ToDoItem.objects.filter(task_name=task_name)

			if not duplicates:
				ToDoItem.objects.create(task_name = task_name, description =description, date_created = timezone.now(), user_id = request.user.id)
				return redirect("todolist:index")

			else:
				context ={
					"error" : True
				}

	return render(request, "todolist/add_task.html", context)	


def update_task(request, todoitem_id):
	todoitem = ToDoItem.objects.filter(pk = todoitem_id)

	context = {
		"user" : request.user,
		"todoitem_id": todoitem_id,
		"task_name": todoitem[0].task_name,
		"description": todoitem[0].description,
		"status": todoitem[0].status
	}

	if request.method == 'POST':
		form = UpdateTaskForm(request.POST)

		if form.is_valid() == False:
			form = UpdateTaskForm()
		else:
			task_name = form.cleaned_data['task_name']
			description = form.cleaned_data['description']
			status = form.cleaned_data['status']

			if todoitem:
				todoitem[0].task_name = task_name
				todoitem[0].description = description
				todoitem[0].status = status

				todoitem[0].save()

				return redirect("todolist:index")

			else:
				context ={
					"error": True
				}

	return render(request, "todolist/update_task.html", context)

def delete_task(request, todoitem_id):
	todoitem = ToDoItem.objects.filter(pk = todoitem_id).delete()

	return redirect("todolist:index")