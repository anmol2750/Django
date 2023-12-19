from django.shortcuts import render


def learn_django(request):
    return render(request,'courseone.html')

def learn_python(request):
    return render(request,'coursetwo.html')