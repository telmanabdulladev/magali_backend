from django.urls import path
from . import views
app_name = "magali_app"

urlpatterns = [
    path("index/", views.index, name="index"),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about,name='about'),
    path('sale/',views.sale,name="sale"),
    path('marketing/',views.marketing,name="marketing"),
    path('consulting/',views.consulting,name="consulting"),
    path('unitdetail/<int:id>/',views.unitdetail,name="unitdetail"),
    path('servicedetail/<int:id>/',views.servicedetail,name="servicedetail"),
    path('messages/',views.contactmessages,name="messages"),


    
]
