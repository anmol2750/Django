from django.shortcuts import render

# Create your views here.
def setcookie(request):
    response = render(request, 'setcookie.html')
    response.set_cookie('name','Akash', max_age=20)
    return response

def getcookie(request):
    # name = request.COOKIES['name']
    name = request.COOKIES.get('name', default = "No Cookie")
    return render(request, 'getcookie.html', {'name':name})

def delcookie(request):
    response = render(request, 'delcookie.html')
    response.delete_cookie('name')
    return response