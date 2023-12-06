from django.shortcuts import render,HttpResponse
from .forms import EmployeeForm

# Create your views here.

def empregistration(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Employee is successfully register.')
    else:
        form = EmployeeForm()
        context = {
            'form':form,
        }
    return render(request, 'form.html', context)
