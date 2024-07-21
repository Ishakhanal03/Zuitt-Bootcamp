from django.urls import path
from . import views
# The path() function can receive for arguments
# We'll only focus on the two arguments that are required, which are the "route" and view, and the third argument name which allows us to make global changes to the url patterns of your project while only touching a single file.
app_name = 'todolist'
urlpatterns=[
    path('',views.index,name="index"),
    # /todolist/todoitem_id route
	# The <int:todoitem_id> allows for creating a dynamic link where the todoitem is provided
	path('<int:todoitem_id>/', views.todoitem, name = 'viewtodoitem'),
	path('register/', views.register, name = "register"),
    path('change_password/', views.change_password, name = "change_password"),
	path('login/', views.login_view, name= "login"),
	path('logout/', views.logout_view, name = "logout"),
    path('add_task/', views.add_task, name = "add_task"),
    path('<int:todoitem_id>/edit', views.update_task, name = "update_task"),
    path('<int:todoitem_id>/delete', views.delete_task, name = "delete_task")
]