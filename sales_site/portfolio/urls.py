from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.get_main_profile_page),
    path('<int:number>/', views.get_projects_by_number),
    path('<title>/', views.get_projects_by_title, name="portfolio-projects"),
]
