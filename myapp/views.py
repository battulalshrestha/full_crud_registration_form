from django.shortcuts import render,redirect
from .models import Item
# Create your views here.
from django.http import HttpResponse
'''def index(request):
    return render(request,'hi.html')
    
# def homepage(request):
if request.method == "POST":
  return JsonResponse({"hello": world})   # in key value pair
    
    '''
#new
def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email= request.POST['email']
        address = request.POST['address']
        password = request.POST['password']
        data =  Item.objects.create(name = name,email =email,address= address,password= password)
        return redirect('hi')
    data = Item.objects.all()
    return render(request,"hi.html", {'key_name':data}) 
        #print(name)
    