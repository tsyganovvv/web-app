from django.urls import path
from . import views

urlpatterns = [
    path('', views.reg),
    path('home', views.home),
    path('shop', views.shop),
    path('neural_network', views.neural_network),
    path('about', views.about)
]
