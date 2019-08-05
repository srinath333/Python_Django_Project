from django.http import HttpResponse, JsonResponse
import datetime
from django.shortcuts import render
from raters_app.forms import signUp,Login
from raters_app.models import *
import random
import random

def index(request):
    return render(request,"raters_app/index.html")
    
def registration(request):
    print("yo")
    if(request.method=="GET"):
        context={
            "form":signUp()
        }
        return render(request,"raters_app/registration.html",context)

    if(request.method=="POST"):
        print("POST")
        x=random.choice(list(range(1,5)))
        raters.objects.create(UID=request.POST["ID"],location=request.POST["location"],age=request.POST["age"],gender=request.POST["gender"],Workflow=x)

        return JsonResponse({"Status":"Saved Successfully",
                             "With Workflow":x
                             })

'''
def login(request):
    print("yo")
    if(request.method=="GET"):
        context={
            "form":Login()
        }
        return render(request,"raters_app/login.html",context)

    if(request.method=="POST"):
        print("POST")
        ra=raters.objects.get(UID=request.POST["ID"])
        text="Welcome"+request.POST["ID"]+" your assigned workflow is "+str(ra.Workflow)

        return JsonResponse({"message":text
                             })
'''

# Create your views here.
