from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('home', views.home),
    path('shop', views.shop),
    path('neural_netork', views.neural_network),
    path('about', views.about)
]
