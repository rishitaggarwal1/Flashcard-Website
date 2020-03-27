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
        correct_ans = int(old_num_1)+int(old_num_2)
        answer = request.POST['answer']
        if int(answer) == correct_ans:
            checker = "Correct!"
            alert = "alert-success"
            statement = old_num_1 + " + " + old_num_2 + " = "+str(correct_ans)
        else:
            checker = "Incorrect!"
            alert = "alert-danger"
            statement = old_num_1 + " + " + old_num_2 + " = "+str(correct_ans)
        return render(request, 'add.html', {
            'answer': answer,
            'checker': checker,
            'alert': alert,
            'statement': statement,
            'num_1': num_1,
            'num_2': num_2
        })
    return render(request, 'add.html', {
        'num_1': num_1,
        'num_2': num_2
    })


def subtract(request):
    from random import randint

    num_1 = randint(51, 100)
    num_2 = randint(0, 50)
    if request.method == "POST":
        old_num_1 = request.POST['num_1']
        old_num_2 = request.POST['num_2']
        correct_ans = int(old_num_1)-int(old_num_2)
        answer = request.POST['answer']
        if int(answer) == correct_ans:
            checker = "Correct!"
            alert = "alert-success"
            statement = old_num_1 + " + " + old_num_2 + " = "+str(correct_ans)
        else:
            checker = "Incorrect!"
            alert = "alert-danger"
            statement = old_num_1 + " + " + old_num_2 + " = "+str(correct_ans)
        return render(request, 'subtract.html', {
            'answer': answer,
            'checker': checker,
            'alert': alert,
            'statement': statement,
            'num_1': num_1,
            'num_2': num_2
        })
    return render(request, 'subtract.html', {
        'num_1': num_1,
        'num_2': num_2
    })


def multiply(request):
    return render(request, 'multiply.html', {})


def divide(request):
    return render(request, 'divide.html', {})
