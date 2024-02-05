from django.urls import path
from . import views

urlpatterns = [
    path('', views.scrape, name='index'),
    path('delete/', views.clear, name='clear')
]
