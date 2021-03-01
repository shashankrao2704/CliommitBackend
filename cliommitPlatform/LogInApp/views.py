from django.shortcuts import render, redirect
from .models import LogIn, RegistrationData
from .forms import RegistrationForm
from django.shortcuts import HttpResponse


# Create your views here.
def LogInPage(request):
    context = {
        "name": "cliommit"
    }
    return render(request, 'Login/login.html', context)


def Home(request, year):
    users_list = LogIn.objects.filter(pub_date__year=year)
    context = {
        "year": year,
        "users_list": users_list,
        "list": ["Python", "Java", "C++", "Git", "Jenkins", "Matlab"]
    }
    return render(request, 'home.html', context)


def register(request):
    context = {
        "form": RegistrationForm
    }
    return render(request, 'signup.html', context)


def addUser(request):
    form = RegistrationForm(request.POST)

    if form.is_valid():
        myRegister = RegistrationData(username=form.cleaned_data['username'],
                                      password=form.cleaned_data['password'],
                                      email=form.cleaned_data['email'],
                                      phone=form.cleaned_data['phone'],
                                      company=form.cleaned_data['company'],
                                      country=form.cleaned_data['country'],
                                      address=form.cleaned_data['address'],
                                      reg_no=form.cleaned_data['reg_no'],
                                      employees=form.cleaned_data['employees'],
                                      sector=form.cleaned_data['sector'],
                                      turnover=form.cleaned_data['turnover'],
                                      electricity=form.cleaned_data['electricity'],
                                      air_travel=form.cleaned_data['air_travel'],
                                      automobile=form.cleaned_data['automobile'],
                                      public_transport=form.cleaned_data['public_transport'],
                                      travel_accommodation=form.cleaned_data['travel_accommodation'],
                                      waste=form.cleaned_data['waste'],
                                      water=form.cleaned_data['water'],
                                      )
        myRegister.save()

    return redirect('login')


