from django.urls import path
from .views import *

urlpatterns = [

    path('', index),
    path('detail/<int:id>', detail, name='detail'),
    path('', home, name='home'),
    path('search/', search, name='search'),
]
