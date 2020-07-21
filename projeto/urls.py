from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('hello/', hello),
    path('funcao/<str:nome>/', funcao),
    path('admin/', admin.site.urls),
]


