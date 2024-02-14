from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import User, Course

# Create your views here.
def index(req):
    return render(req, 'app/index.html')

def academics_view(req):
    return render(req, 'app/academics.html')

def all_course_view(req):
    courses = Course.objects.all()
    return render(req, 'app/all_course.html', {
        'courses': courses
    })

def create_course(req):
    if req.method == 'POST':
        coursetitle = req.POST['title']
        try:
            newcourse = Course.objects.create(
                title = coursetitle
            )
        except IntegrityError as err:
            print(err)
            return render(req, 'app/create_course.html', {
                'message': 'A course with this name already exists'
            })
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(req, 'app/create_course.html')

def register(req):
    if req.method == 'POST':
        firstname = req.POST['firstname']
        lastname = req.POST['lastname']
        username = req.POST['username']
        password = req.POST['password']
        is_staff = req.POST['is_staff']
        confirmation = req.POST['conf']
        if password != confirmation:
            return render(req, 'app/register.html', {
                'message': 'Password must match'
            })
        
        try:
            email = username + '@app.com'
            user = User.objects.create_user(
                first_name = firstname,
                last_name = lastname,
                username = username,
                password = password,
                email = email,
                is_staff = is_staff
            )
        except IntegrityError as err:
            print(err)
            return render(req, 'app/register.html', {
                'message': 'username already taken'
            })
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(req, 'app/register.html')
    
def logout_view(req):
    logout(req)
    return HttpResponseRedirect(reverse('login'))

def login_view(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(req, username=username, password=password)

        if user is not None:
            login(req, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(req, 'app/login.html', {
                'message': 'Invalid username or password'
            })
    else:
        return render(req, 'app/login.html')
    