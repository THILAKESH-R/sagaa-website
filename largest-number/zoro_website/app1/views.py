from django.shortcuts import render
from django.http import *

# Create your views here.

def homepage(request):
    return render(request,"process.html")

#Logic for receving custreg from data
def iprocess (request):
    number1 = request.POST.get("First number")
    number2 = request.POST.get("Second number")
    number3 = request.POST.get("Third number")
    
    print(number1 ,"",number2 ,"",number3, "")
    if number1>number2 and number1>number3:
        max=number1
    elif number2>number3:
        max=number2
    else:
        max=number3        

    return HttpResponse (f"<h2> the maximum number is {max} ")


