from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm


def home(request):
    if request.method == 'POST':
        # passing the form data to LoginForm
        user_details = UserForm(request.POST)
        # validating the user_details with is_valid() method
        if user_details.is_valid():
            # writing data to the database
            user_details.save()
            # redirect to another page with success message
            return HttpResponse("Data submitted successfully")
        else:
            # redirect back to the user page with errors
            return render(request, 'home.html', {'form':user_details})
    else:
        # in case of GET request
        form = UserForm(None)
        return render(request, 'home.html', {'form':form})