from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
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
def show_data(request):
    datas = Register.objects.all()
    context = {'value':datas}
    
    return render(request,'show_data.html',context)

def delete_data(request,id):
    data = Register.objects.get(id= id)
    data.delete()
    return redirect('show_data')
def edit_data(request,id):
     item = get_object_or_404(Register, id=id)

     if request.method == "POST":
        # Get updated data from the form
        item.name = request.POST.get('name')
        item.email = request.POST.get('email')
        item.password = request.POST.get('password')
        item.confirm_password = request.POST.get('confirm_password')

        # Perform basic validation
        if item.password == item.confirm_password:
            item.save()  # Save the changes
            return redirect('show_data')  # Redirect after editing
        else:
            # Add an error message if passwords do not match
            error_message = "Passwords do not match."
            return render(request, 'edit_template.html', {'item': item, 'error_message': error_message})

    # Render the form with existing item data if GET request
     return render(request, 'edit_template.html', {'item': item})