from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from magali_app.models import SettingsModel,ConsultingUnitModel,ServicesModel,ContactModel,CTCategoryModel,CorporativeTrainingModel,ConsultingModel
from django.http import Http404


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
    services=ServicesModel.objects.all()
    context = {
        "settings": settings,
        "services": services,
    }
    return render(request,"haqqimizda.html",context)

def sale(request):
    # corporative = CorporativeTrainingModel.objects.all()
    ctcategory = get_object_or_404(CTCategoryModel,name="Satış")
    context = {
        "ctcategory":ctcategory
    }
    # context["corporative"] = corporative
    return render(request,'sale.html', context)

def marketing(request):
    # corporative = CorporativeTrainingModel.objects.all()
    ctcategory = get_object_or_404(CTCategoryModel, name="Marketing və HR")
    context = {
        "ctcategory":ctcategory
    }
    # context["corporative"] = corporative
    return render(request,'marketing.html', context)

def consulting(request):
    consulting = get_object_or_404(ConsultingModel, name="Konsaltinq")
    context = {
        "consulting":consulting
    }
    return render(request,"consulting.html",context)

def unitdetail(request,id):
    unit = get_object_or_404(ConsultingUnitModel, id=id)
    context = {
        "unit":unit
    }
    return render(request,"unit_detail.html",context)

def servicedetail(request, id):
    service = get_object_or_404(ServicesModel, id = id)
    context = {
        "service":service
    }
    return render(request,"servicedetail.html",context)

def contactmessages(request):
    if not request.user.is_staff:
        raise Http404
    else:
        messages = ContactModel.objects.all()
        context = {
            "messages":messages
        }
    return render(request,"messages.html",context)


    












    
