from django import urls
from django.urls import path
from django.urls.conf import include
from rango import views


app_name = 'rango'
urlpatterns=[
    path('',views.index,name='index'),
    path('about/', views.about, name='about'),
]
