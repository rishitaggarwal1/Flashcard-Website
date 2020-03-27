from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


def add(request):
    return render(request, 'add.html', {})


def subtract(request):
    return render(request, 'subtract.html', {})


def multiply(request):
    return render(request, 'multiply.html', {})


def divide(request):
    return render(request, 'divide.html', {})
