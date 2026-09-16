from django.urls import path

from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stats/', views.stats, name='stats'),
]