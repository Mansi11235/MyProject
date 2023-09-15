from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello from index")

def home(request):
    return HttpResponse("Hello from home")

def contact(request):
    return HttpResponse("Hello from contact")