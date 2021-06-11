from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PostForm, LoginForm, UserForm, SignupForm
from .models import Post, Contact, Profile
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


def about(request):
    return render(request, 'blog/about.html')

def services(request):
    return render(request, 'blog/services.html')


def addpost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        else:
            form = PostForm()
        return render(request, 'blog/addpost.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')


def update_post(request, id):
    if request.method == 'POST':
        data = Post.objects.get(pk=id)
        form = PostForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        data = Post.objects.get(pk=id)
        form = PostForm(instance=data)
    return render(request, 'blog/updatepost.html', {'form': form, 'data': data})


def show_post(request, id):
    if request.user.is_authenticated:
        data = Post.objects.get(pk=id)
        return render(request, 'blog/showpost.html', {'data': data})
    else:
        return HttpResponseRedirect('/login/')


def user_signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account Created Sucessfully!')
            user = form.save()
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'blog/signup.html', {'form': form})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Loged in Sucessfully!')
                    return HttpResponseRedirect('/')

        else:
            form = LoginForm()
        return render(request, 'blog/login.html', {'form': form})
    else:
        return HttpResponseRedirect('/')


def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out Sucessfully ! ')
    return HttpResponseRedirect('/')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        message = request.POST.get('Message')
        c = Contact(name=name, email=email, message=message)
        c.save()
        messages.success(request, 'Your response has been send Sucessfully!')
        return HttpResponseRedirect('/contact/')
    return render(request, 'blog/contact.html')


def show_profile(request, id):
    data = User.objects.get(pk=id)
    all_users = User.objects.all()
    return render(request, 'blog/profile.html', {'data': data, 'all_users': all_users})


def edit_profile(request, id):
    if request.method == 'POST':
        p = User.objects.get(pk=id)
        fm = UserForm(request.POST, instance=p)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Profile Updated Sucessfully!')
            return HttpResponseRedirect('/')
    else:
        p = User.objects.get(pk=id)
        fm = UserForm(instance=p)
    return render(request, 'blog/editprofile.html', {'form': fm})


def change_password(request):
    if request.method == 'POST':
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request, fm.user)
            messages.success(request, 'Password Changed Sucessfully!')
            return HttpResponseRedirect('/')
    else:
        fm = PasswordChangeForm(user=request.user)
    return render(request, 'blog/changepass.html', {'form': fm})


def delete_user(request, id):
    if request.method == 'POST':
        p = User.objects.get(pk=id)
        p.delete()
    return HttpResponseRedirect('/')


def delete_post(request, id):
    if request.method == "POST":
        data = Post.objects.get(pk=id)
        data.delete()
    return HttpResponseRedirect('/')
