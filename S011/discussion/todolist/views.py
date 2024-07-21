from django.shortcuts import render, redirect, get_object_or_404

# Import the ToDoItem model
from .models import ToDoItem, EventItem

# Importing the pre-created user Model
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

from django.forms.models import model_to_dict

from .forms import LoginForm, AddTaskForm, UpdateTaskForm,RegisterForm,AddEventForm,UpdateEventForm,UpdateProfile

from django.utils import timezone

# Create your views here.

def index(request):
	if request.user.is_anonymous:
		return redirect('todolist:login')
	else:
		todoitem_list = ToDoItem.objects.filter(user_id = request.user.id)
		eventitem=EventItem.objects.filter(user_id=request.user.id)
		context = {
			'user': request.user,
			'todoitem_list': todoitem_list,
			'eventitem':eventitem
		}
	return render(request, "todolist/index.html", context)

def todoitem(request, todoitem_id):
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


def login_view(request):
	context = {}
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid() == False:
			form = LoginForm()
			context={
				'error':True
            }
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
			context={
				'error':True
			}
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

def add_event_view(request):
    if request.user.is_anonymous:
        return redirect('todolist:login')
    else:
        context={}
        if(request.method=="POST"):
            form=AddEventForm(request.POST)
            if(form.is_valid()==False):
                form=AddEventForm()
                context={
                    'error':True,
                    'msg':"Form Invalid"
                }
            else:
                event_name=form.cleaned_data['event_name']
                description=form.cleaned_data['description']
                event_date=form.cleaned_data['event_date']
                duplicates=EventItem.objects.filter(event_name=event_name)
                if not duplicates:
                    EventItem.objects.create(event_name=event_name,description=description,event_date=event_date,user_id=request.user.id)
                    return redirect("todolist:index")
                else:
                    context={
                        'error':True,
                        'msg':"Duplicates Event"
                    }
        return render(request,'todolist/add_event.html',context)
def eventitem_view(request,eventitem_id):
    if request.user.is_anonymous:
        return redirect("todolist:login")
    else:
        eventitem=get_object_or_404(EventItem,pk=eventitem_id)
        return render(request,'todolist/vieweventitem.html',model_to_dict(eventitem))
def delete_eventitem(request,eventitem_id):
    if request.user.is_anonymous:
        return redirect("todolist:login")
    else:
        EventItem.objects.filter(pk=eventitem_id).delete()
        return redirect("todolist:index")
def update_eventtask(request,eventitem_id):
    if request.user.is_anonymous:
        return render("todolist:login")
    else:
        item=EventItem.objects.filter(pk=eventitem_id)
        context={
            'event_name':item[0].event_name,
            'description':item[0].description,
            'status':item[0].status,
            'event_date':item[0].event_date
        }
        if(request.method=="POST"):
            form=UpdateEventForm(request.POST)
            if(form.is_valid()==False):
                form=UpdateEventForm()
                context={
                    'error':True
                }
            else:
                event_name=form.cleaned_data['event_name']
                description=form.cleaned_data['description']
                event_date=form.cleaned_data['event_date']
                status=form.cleaned_data['status']
                if item:
                    item[0].event_name=event_name
                    item[0].description=description
                    item[0].event_date=event_date
                    item[0].status=status
                    item[0].save()
                    return redirect("todolist:index")
                else:
                    context={
                        'error':True
                    }
        return render(request,'todolist/update_event.html',context)
def update_profile(request):
    if(request.user.is_anonymous):
        return redirect("todolist:login")
    else:
        context={
            'error':False,
            'msg':"",
            'username':request.user.username,
            'first_name':request.user.first_name,
            'last_name':request.user.last_name,
            'email':request.user.email,
        }
        if(request.method=="POST"):
            form=UpdateProfile(request.POST)
            if(form.is_valid()==False):
                form=UpdateProfile()
                context={
                    'error':True,
                    'msg':"Form is invalid! Try Again",
                    'username':request.user.username,
                    'first_name':request.user.first_name,
                    'last_name':request.user.last_name,
                    'email':request.user.email,
                    }
            else:
                previous_password=form.cleaned_data['previous_password']
                password=form.cleaned_data['password']
                confirm_password=form.cleaned_data['confirm_password']
                user=authenticate(username=request.user.username,password=previous_password)
                if user is not None:
                    if(password==confirm_password):
                        user.set_password(password)
                        user.save()
                        logout(request)
                        return redirect('todolist:index')
                    else:
                        context={
                        'error':True,
                        'msg':"Enter same new password",
                        'username':request.user.username,
                        'first_name':request.user.first_name,
                        'last_name':request.user.last_name,
                        'email':request.user.email,
                        }


        return render(request,"todolist/update_profile.html",context)