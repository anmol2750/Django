from django.http import HttpResponse

def fees_django(request):
    return HttpResponse('300')

def fees_python(request):
    return HttpResponse('200')

