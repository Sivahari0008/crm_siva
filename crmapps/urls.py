from django.urls import path,include
from django.conf.urls import url
from . import views

urlpatterns=[        
    path('',views.add,name='add'),
    path('forms5.html',views.sub,name='sub'),
    path('forms4.html',views.add,name='add'),
]