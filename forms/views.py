from ast import Return
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    print(request.POST)
    # return HttpResponse("hello")
    return render(request, 'forms/index.html')

def data(request):
    name = request.GET.get('name')
    password = request.GET.get('password')
    address = request.GET.get('address')
    city = request.GET.get('city')
    gender = request.GET.get('gender')
    Vehicle = request.GET.getlist('Vehicle')
    Salary = request.GET.get('Salary')
    dateOfBirth=request.GET.get('dateOfBirth')
    
    return render(request, 'forms/data1.html',{'name':name , 'password':password , 'address':address , 'city':city , 'gender':gender , 'Vehicle':Vehicle,'Salary':Salary,'dateOfBirth':dateOfBirth})