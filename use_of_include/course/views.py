from django.http import HttpResponse

# Create your views here.

def learn_django(request):
    return HttpResponse('<h1> Learn Django </h1>')

def learn_python(request):
    return HttpResponse('<h1> Learn Python </h1>') 