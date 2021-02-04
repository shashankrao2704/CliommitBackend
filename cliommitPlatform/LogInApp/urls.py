from django.urls import path
from .views import LogIn, Home
urlpatterns = [
    path('login/', LogIn, name ="login"),
    path('home/', Home, name="home")
]