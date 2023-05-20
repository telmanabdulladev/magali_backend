from django.shortcuts import render
from django.contrib.auth.models import User
from magali_app.models import SettingsModel,ServicesModel,ContactModel,CTCategoryModel,CorporativeTrainingModel


# Create your views here.

def index(request):
    settings = SettingsModel.objects.first()
    services = ServicesModel.objects.all()
    context = {
        "settings":settings,
    }
    context["services"] = services   
    return render(request,"index.html",context)

def contact(request):
   if request.method=="POST":
       first_name=request.POST['first_name']
       last_name=request.POST['last_name']
       company_name=request.POST['company_name']
       email=request.POST['email']
       phone_num=request.POST['phone_num']
       message=request.POST['message']
    #    contact modelin xussiyetlerini gonderdiyimiz ucun contact modelinin obyektini yaradiriq
       ContactModel.objects.create(
           first_name=first_name,
           last_name=last_name,
           company_name=company_name,
           email=email,
           phone_num=phone_num,
           message=message,      
        )
   return render(request,"contact.html")

def about(request):
    settings= SettingsModel.objects.first()
    context = {
        "settings": settings
    }
    return render(request,"haqqimizda.html",context)

def sale(request):
    # corporative = CorporativeTrainingModel.objects.all()
    ctcategories = CTCategoryModel.objects.all()
    context = {
        "ctcategories":ctcategories
    }
    # context["corporative"] = corporative
    return render(request,'sale.html', context)

def marketing(request):
    # corporative = CorporativeTrainingModel.objects.all()
    ctcategory = CTCategoryModel.objects.first()
    context = {
        "ctcategory":ctcategory
    }
    # context["corporative"] = corporative
    return render(request,'sale.html', context)




    
