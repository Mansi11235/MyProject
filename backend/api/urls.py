from django.urls import path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index),
    path('home/', views.home),
    path('contact/', views.contact)
]

urlpatterns = format_suffix_patterns(urlpatterns)