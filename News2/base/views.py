from django.shortcuts import render, redirect
from .models import Topic, News, Comment
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db.models import Q

def HomePage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.all()
    news = News.objects.filter(
        Q(topic__name__icontains=q) |
        Q(content__icontains=q)
    )
    context = {'topics':topics, 'news': news}
    return render(request, 'base/index.html', context)

def LoginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':    
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            message = messages.error(request, "This username dose not exist")
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "username or password dose not match")
    context = {'page':page}
    return render(request, 'base/loginregister.html', context)

def LogoutUage(request):
    logout(request)
    return redirect('home')

def RegisterPage(request):
    page = 'register'
    context = {}
    return render(request, 'base/loginregister.html', context)

def FavoritePage(request, pk):
    context = {}
    return render(request, 'base.favorite.html', context)

def TopicsPage(request):
    topics = Topic.objects.all()
    context = {'topics':topics}
    return render(request, 'base/topics.html', context)

def createnewsPage(request):
    context = {}
    return render(request, 'base/createnews.html', context)

