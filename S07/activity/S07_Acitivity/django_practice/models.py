from django.db import models

# Create your models here.
class GroceryItem(models.Model):
    item_name = models.CharField(max_length= 50)
    category = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default = "pending")
    date_created = models.DateTimeField('data created')