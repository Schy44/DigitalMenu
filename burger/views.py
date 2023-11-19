from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.shortcuts import render, redirect
from .models import MenuItem
from django.contrib.auth.forms import UserCreationForm
from .models import Userprofile
from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def burger(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('user_login')

    return render(request, 'signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')


def logout(request):
    logout(request)
    return redirect('login')


def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def view(request):
    menuItems = MenuItem.objects.all()
    template = loader.get_template('view.html')
    context = {
        'menuitems': menuItems,
    }
    return render(request, 'view.html', context)


def temp(request):
    template = loader.get_template('template.html')
    return HttpResponse(template.render())


def menu(request):
    burgerMenus = BurgerMenu.objects.all()
    chefSpecials = ChefSpecial.objects.all()
    context = {
        'chefSpecials': chefSpecials,
        'burgerMenus': burgerMenus,
    }
    return render(request, 'menu.html', context)
