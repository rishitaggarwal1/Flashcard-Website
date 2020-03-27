from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


def add(request):
    from random import randint

    num_1 = randint(0, 100)
    num_2 = randint(0, 100)
    if request.method == "POST":
        old_num_1 = request.POST['num_1']
        old_num_2 = request.POST['num_2']
        ans = old_num_1+old_num_2
        answer = request.POST['answer']
        return render(request, 'add.html', {'answer': answer})
    return render(request, 'add.html', {
        'num_1': num_1,
        'num_2': num_2
    })


def subtract(request):
    return render(request, 'subtract.html', {})


def multiply(request):
    return render(request, 'multiply.html', {})


def divide(request):
    return render(request, 'divide.html', {})
