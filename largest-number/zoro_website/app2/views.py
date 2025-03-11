from django.shortcuts import render
from django.http import *

# Create your views here.

def homepage(request):
    return render(request,"regform.html")

#Logic for receving custreg from data
def register (request):
    name = request.POST.get("name")
    father_name = request.POST.get("father_name")
    gender = request.POST.get("gender")
    address = request.POST.get("address")
    pincode = request.POST.get("pincode")
    phone = request.POST.get("phone")
    qualification = request.POST.get("qualification")
    hobbies= request.POST.get("hobbies")
    description= request.POST.get("description")

    return HttpResponse(f"NAME= {name} <br> FATHER NAME={father_name} <br> GENDER = {gender} <br> ADDRESS = {address} <br> PINCODE = {pincode} <br> QUALIFICATION = {qualification} <br> HOBBIES = {hobbies} <br> DESCRIPITON = {description}")


