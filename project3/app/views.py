from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.

def register(request):
    name = 'Diptiman'
    pno = 8018387476
    email = 'diptimannayak2001@gmail.com'
    add = 'Bhubaneswar'
    EO = Emp(ename= name, pno = pno , email = email , add= add)
    return HttpResponse('Employee registered successfully')

def register(request):
    if request.method =='POST':
        name = request.POST.get('ename')
        pno = request.POST.get('pno')
        email=request.POST.get('email')
        add=request.POST.get('add')
        print(name,pno,email,add)

        EO = Emp(ename=name,pno=pno,email=email,add=add)
        EO.save()

        return HttpResponse('Empoyee Registered Successfully')
    return render(request,'my.html')



def home(request):
    name='Diptiman'
    phno=8018387476
    d={'name':name,'phno':phno}
    EO = Emp.objects.all
    d={'EmployeeObjects':EO}
    return render(request,'home.html')