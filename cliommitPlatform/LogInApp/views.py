from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
def LogIn(request):
    return render(request, 'Login/login.html', )


def Home(request):
    return render(request, 'home.html')
