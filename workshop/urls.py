from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('workshoplist/<str:pk>/', views.workshoplist, name="workshoplist"),
    path('create/', views.workshop_create, name="workshop_create"),
    path('newcategory/', views.category_create, name="category_create"),
    path('detail/<str:pk>/', views.workshop_detail, name="workshop_detail"),


]
