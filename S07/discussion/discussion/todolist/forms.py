from django import forms

class LoginForm(forms.Form):
    username= forms.CharField(label= 'username', max_length=20)
    password= forms.CharField(label='password', max_length= 20)

class AddTaskForm(forms.Form):
    task_name = forms.CharField(label= 'task_name', max_length=50)
    description= forms.CharField(label= 'description', max_length=200)

class UpdateTaskForm(forms.Form):
    task_name = forms.CharField(label='task_name', max_length= 50)
    description = forms.CharField(label='description', max_length= 200)
    status = forms.CharField(label='status', max_length= 50)

class RegisterForm(forms.Form):
    username=forms.CharField(label="username",max_length=50)
    firstname=forms.CharField(label="first_name",max_length=50)
    lastname=forms.CharField(label="last_name",max_length=50)
    email=forms.CharField(label="email",max_length=50)
    password=forms.CharField(label="password",max_length=50)
    confirm_password=forms.CharField(label="confirm_password",max_length=50)