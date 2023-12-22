from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def stockPicker(request):
    
    return HttpResponse("Hey I am picking stocks")