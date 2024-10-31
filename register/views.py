from django.shortcuts import render,redirect
from .models import Register
from django.contrib import messages
# Create your views here.
def home(request):
    #return render(request,'register.html')
    if request.method == "POST":
        name = request.POST['name']
       # print(name)
        email = request.POST['email']
        #print(email)
        password = request.POST['password']
        #print(password)
        confirm_password = request.POST['confirm_password']
       # print(confirm_password)
        user = Register(name = name,email =email,password= password,confirm_password = confirm_password)
        user.save()
        messages.success("your form has been submitted successfully")
    return render(request,'register.html')
