from django.urls import path
from . import views

urlpatterns=[
    path("",views.homepage,name="home"),
     path('inputprocess',views.iprocess, name="inputprocess"),
   
]


from . import views