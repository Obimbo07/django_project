from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<div><h1>Vickie</h1><p>Welcome to kenya!</p></div>')

def about(request):
    return HttpResponse('<div><h1>About<h1></div>')