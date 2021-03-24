from django.urls import path
from .views import LogInPage, loginValidation, Home, register, addUser, carbonRegistration, addCarbonData
urlpatterns = [
    path('login/', LogInPage, name ="login"),
    path('loginCheck/', loginValidation, name ="loginCheck"),
    path('home/<int:id>', Home, name="home"),
    path('signup/', register, name="register"),
    path('addUser/', addUser, name="addUser"),
    path('addCarbon/', carbonRegistration, name="addCarbon"),
    path('addCarbonData/', addCarbonData, name="addCarbonData"),
]