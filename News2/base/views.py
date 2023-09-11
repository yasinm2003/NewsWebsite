from django.shortcuts import render
from .models import Topic, News, Comment
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
    context = {}
    return render(request, 'base/loginregister.html', context)

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

