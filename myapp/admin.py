from django.contrib import admin
from .models import Item
# Register your models here.

admin.site.register(Item)
'''
to retrive only one data
use get () method
a = Classname.objects.all() # where the data are stored
a = Classname.objects.get(id = 1)

to retrive more than one data use filter method
a= Classname.objects.filter(id =5)
 does not raise exception if data is not present
 to insert(update or adding something) or add data 
 a = classname(name = "nishan",email = "ram@gmail.com",address = "rautepani")
 a.save() saving the above data in the database
 also can do this
 a= classname.object.create(name = "nishan",email ="email@.com",address = "anyplace")
 # now updating above data
 a = classname.objects.filter(id =4).update(name = "anyname") --> use filter with this id name and .update function()
 deleting above data
 a = classname.objects.all()
 a.delete()
  for one data
  a = classname.objects.get(id = 4)
  a.delete()
  for deleting one or so more than one data
  a = classname.objects.filter(id__in=[3,4])
  a.delete()

  to retrive the all the name from database start with 's'
  a= home.objects.filter(name_startswith = "s")

  to retrive all that email start with contain '@hotmail.com" from database
  a= classname.objects.filter(email_endswith= "@gmail.com")
  for like facebook / google searchbar

  for serching on the database
  like retriving the data who lives in kathmandu 
  a = classname.objects.filter(address_icontains = "gorkha")
  a = classname.objects.filter(email_icontains = "@gmail.com")
  a= home.objecfs.filter(name_icontains = "nishan")
  

  



'''