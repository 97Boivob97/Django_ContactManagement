from django.urls import path
from .import views
urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("add/",views.add,name="add"),
    path("update/<int:pk>/",views.update,name="update"),
    path("delete/<int:pk>/",views.delete,name="delete"),
    path('search/', views.search, name='search'), 
 
 ]