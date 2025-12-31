from django.urls import path
from .views import *

urlpatterns = [
    path('setup_qadaa/', setup_qadaa, name='setup_qadaa'),
    path('prayers_list/', prayers_list, name='prayers_list'),
]