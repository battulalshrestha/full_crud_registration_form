from django.db import models

# Create your models here.
class Item(models.Model):
 name = models.CharField(max_length=50)
 email = models.EmailField(unique=True)
 address= models.CharField(max_length=60)
 password = models.CharField(max_length=50)
 def __str__(self):
  return self.name