from django.urls import path
from .import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('home/',views.home,name="home"),
    path('login/',views.sign_in,name="login"),
]
