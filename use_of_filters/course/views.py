from django.shortcuts import render

def add(request):
    return render(request,'course/add.html',{'fruits':['Apple','Banana','Cherry']})

def addslashes(request):
    return render(request,'course/addslashes.html',{'name': "Capt'n Jack"})

def capfirst(request):
    return render(request,'course/capfirst.html',{'animal': 'lion'})

def center(request):
    return render(request,'course/center.html',{'name': 'Social'})

def first(request):
    return render(request,'course/first.html',{'fruits':['Apple','Banana','Cherry','Orange']})

def last(request):
    return render(request,'course/last.html',{'fruits':['Apple','Banana','Cherry','Orange']})

def floatformat(request):
    return render(request,'course/floatformat.html',{'p1':56.24323, 'p2':56.000, 'p3':56.37000})

def length(request):
    return render(request,'course/length.html',{'fruits':['Apple','Banana','Cherry','Orange']})

def dictsort(request):
    return render(request,'course/dictsort.html',{'cars': 
    [
      {'brand': 'Ford', 'model': 'Mustang', 'year': 1964},
      {'brand': 'Volvo', 'model': 'XC90', 'year': 2022},
      {'brand': 'Volvo', 'model': 'P1800', 'year': 1962},
      {'brand': 'Ford', 'model': 'Focus', 'year': 2004},
    ]})

def unordered_list(request):
    return render(request,'course/unordered_list.html',{'fruits':['Apple','Banana','Cherry','Orange']})