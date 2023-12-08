from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name'] = 'Vashu'
    return render(request, 'setsession.html')

def getsession(request):
    name = request.session.get('name', default='No Data')
    return render(request, 'getsession.html', {'name':name})

def delsession(request):
    del request.session['name']
    return render(request, 'delsession.html')
    
    