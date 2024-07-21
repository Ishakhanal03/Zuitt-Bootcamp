from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# [Section] Models
# Each model is represented by a class that subclasses django.db.models.Models. Each model has a number of class variables, each of which represents a database field in the model.
class ToDoItem(models.Model):
	task_name = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	status = models.CharField(max_length=50, default = "pending")
	date_created = models.DateTimeField('data created')
	user = models.ForeignKey(User, on_delete = models.CASCADE, default="")