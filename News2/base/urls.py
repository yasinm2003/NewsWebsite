from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name="home"),
    path('login/', views.LoginPage, name="login"),
    path('logout/', views.LogoutUage, name="logout"),
    path('register/', views.RegisterPage, name="register"),
    path('favorite/<str:pk>/', views.FavoritePage, name="favorite"),
    path('createnews/', views.createnewsPage, name="createnews"),
]