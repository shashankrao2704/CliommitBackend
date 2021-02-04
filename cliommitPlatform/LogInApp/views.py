from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def LogIn(request):
    return HttpResponse("<h1>Log In Page</h1>")
def Home(request):
    return HttpResponse("<h1>The Home Page</h1>")
