from django.shortcuts import render
from .models import member

def members(request):
    my_members = member.objects.all().values()
    return render(request, 'members.html', {'mymembers':my_members})

def details(request, slug):
    my_member = member.objects.get(slug=slug)
    return render(request, 'details.html', {'mymember':my_member})

def main(request):
    return render(request, 'main.html')

def queryset(request):
    data = member.objects.filter(lastname='Gupta').values()
    return render(request, 'queryset.html', {'mymember':data})