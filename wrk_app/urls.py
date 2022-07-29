from unicodedata import name
from . import views
from django.urls import path,include



urlpatterns = [
    path('',views.homepage,name='homepage'),
    
    path('wrk',views.wrk,name='wrk'),
]