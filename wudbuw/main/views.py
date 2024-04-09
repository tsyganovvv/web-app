from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request, 'main/index.html')


def home(request):
    return render(request, 'main/home.html')


def shop(request):
    return render(request, 'main/shop.html')


def neural_network(request):
    return render(request, 'main/neural_netork.html')


def about(request):
    return render(request, 'main/about.html')
