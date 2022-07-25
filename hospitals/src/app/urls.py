from django.contrib import admin
from django.urls import path, re_path
from django.urls import re_path as url

#from django.urls import url
from rest_framework.documentation import include_docs_urls
from .views import *

urlpatterns = [ 
                path('hospitals/', hospitals), 
]
