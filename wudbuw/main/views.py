from django.shortcuts import render
from django.http import HttpResponse
from .models import Sneacers


def main(request):
    return render(request, 'main/index.html')


def home(request):
    return render(request, 'main/home.html')


def shop(request):
    sneacers = Sneacers.objects.all
    return render(request, 'main/shop.html', {'sneacers': sneacers})


def neural_network(request):
    return render(request, 'main/neural_netork.html')


def about(request):
    return render(request, 'main/about.html')
