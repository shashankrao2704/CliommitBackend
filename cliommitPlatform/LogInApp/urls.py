from django.urls import path
from .views import LogInPage, Home, register, addUser
urlpatterns = [
    path('login/', LogInPage, name ="login"),
    path('home/<int:year>', Home, name="home"),
    path('signup/', register, name="register"),
    path('addUser/', addUser, name="addUser"),
]