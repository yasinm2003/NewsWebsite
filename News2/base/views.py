from django.shortcuts import render, redirect
from .models import Topic, News, Comment, User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .form import UserForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def HomePage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    if request.user.is_authenticated:
        user = request.user.favorite if request.user.favorite != None else ''
        favorite = News.objects.filter(
        Q(topic__name__icontains=user)
    )
    else:
        favorite = None
    topics = Topic.objects.all()
    news = News.objects.filter(
        Q(topic__name__icontains=q) |
        Q(content__icontains=q)
    )
    context = {'topics':topics, 'news': news, 'favorite':favorite}
    return render(request, 'base/index.html', context)

def LoginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':    
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=username)
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
    form = UserForm()
    context = {'form':form}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Try again')
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

@login_required(login_url='login')
def NewsPage(request, pk):
    news = News.objects.get(id=pk)
    if request.method == 'POST':
        news.like += 1
        news.save()
        liked = True
    else:
        liked = False
    context = {'news':news, 'liked':liked}
    return render(request, 'base/news.html', context)