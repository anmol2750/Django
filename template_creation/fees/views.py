from django.shortcuts import render

def fees_django(request):
    return render(request,'feesone.html')

def fees_python(request):
    return render(request,'feestwo.html')