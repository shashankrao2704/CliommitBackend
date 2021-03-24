from django.shortcuts import render, redirect
from .models import RegistrationData, CarbonData
from .forms import RegistrationForm, CarbonRegistration, LoginForm
from django.shortcuts import HttpResponse


# Create your views here.
def LogInPage(request):
    context = {
        "name": "cliommit",
        "form": LoginForm
    }
    return render(request, 'login.html', context)


def loginValidation(request):
    form = LoginForm(request.POST)
    # registry = RegistrationData.objects.get(id=18)
    # if form.is_valid():
    #     if registry.username == form.cleaned_data['username']:
    #         if registry.password == form.cleaned_data['password']:
    #             return redirect('home')
    #         else:
    #             print("invalid password")
    #     else:
    #         print("invalid username")
    # return redirect('login')
    if form.is_valid():
        username = form.cleaned_data['username']
        if RegistrationData.objects.filter(username=username):
            user = RegistrationData.objects.get(username=username)
            if user.password == form.cleaned_data['password']:
                return redirect('home', user.id)
            else:
                print("invalid password")
        else:
            print("invalid username")
    return redirect('login')



def Home(request, id):
    user_carbon = CarbonData.objects.get(user_id=id)
    context = {
        "user": user_carbon,
    }
    return render(request, 'home.html', context)

def homeToCarbon(request):
    return redirect('addCarbon')


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
                                      )
        myRegister.save()

    return redirect('login')


def carbonRegistration(request):
    registry = RegistrationData.objects.get(id=18)
    context = {
        "form": CarbonRegistration,
        "registry": registry
    }
    return render(request, 'carbon-registration.html', context)


def addCarbonData(request):
    form = CarbonRegistration(request.POST)
    if form.is_valid():
        myCarbonData = CarbonData(user=RegistrationData.objects.get(id=18),
                                  electricity_amount=form.cleaned_data['electricity_amount'],
                                  electricity_renewable=form.cleaned_data['electricity_renewable'],
                                  electricity_provider=form.cleaned_data['electricity_provider'],
                                  electricity_type=form.cleaned_data['electricity_type'],
                                  electricity_heating=form.cleaned_data['electricity_heating'],
                                  electricity_gas=form.cleaned_data['electricity_gas'],
                                  travel_air_travel=form.cleaned_data['travel_air_travel'],
                                  travel_automobile_mileage=form.cleaned_data['travel_automobile_mileage'],
                                  travel_automobile_commute=form.cleaned_data['travel_automobile_commute'],
                                  travel_bus=form.cleaned_data['travel_bus'],
                                  travel_coach=form.cleaned_data['travel_coach'],
                                  travel_train=form.cleaned_data['travel_train'],
                                  travel_int_train=form.cleaned_data['travel_int_train'],
                                  travel_subway=form.cleaned_data['travel_subway'],
                                  travel_tram=form.cleaned_data['travel_tram'],
                                  travel_taxi=form.cleaned_data['travel_taxi'],
                                  travel_accommodation_hotel=form.cleaned_data['travel_accommodation_hotel'],
                                  travel_accommodation_motel=form.cleaned_data['travel_accommodation_motel'],
                                  travel_accommodation_airbnb=form.cleaned_data['travel_accommodation_airbnb'],
                                  travel_accommodation_hostel=form.cleaned_data['travel_accommodation_hostel'],
                                  office_utilities_desktop=form.cleaned_data['office_utilities_desktop'],
                                  office_utilities_laptop=form.cleaned_data['office_utilities_laptop'],
                                  office_waste_bio=form.cleaned_data['office_waste_bio'],
                                  office_waste_battery=form.cleaned_data['office_waste_battery'],
                                  office_waste_plastic=form.cleaned_data['office_waste_plastic'],
                                  office_waste_glass=form.cleaned_data['office_waste_glass'],
                                  office_waste_paper=form.cleaned_data['office_waste_paper'],
                                  office_waste_hardware=form.cleaned_data['office_waste_hardware'],
                                  office_water=form.cleaned_data['office_water'],
                                  )
        myCarbonData.save()

    return redirect('addCarbon')
