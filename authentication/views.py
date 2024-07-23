from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, 'authentication/index.html')


def sign_up(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = first_name
        myuser.last_name = last_name

        myuser.save()

        messages.success(request, "Your Account has been successfully created.")

        return redirect('home')

    return render(request, 'authentication/signup.html')


def sign_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            first_name = user.first_name
            return render(request, 'authentication/index.html', {'first_name': first_name})
        
        else:
            messages.error(request, "Your username or password was incorrect!")
            return redirect('home')

    return render(request, 'authentication/signin.html')


def sign_out(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')
