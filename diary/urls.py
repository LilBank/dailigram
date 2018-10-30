from django.urls import path,  include
from diary import views
from django.contrib.auth import views as auth_views

app_name = 'diary'
urlpatterns = [
    # ex: /diary/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /diary/register/
    path('register/', views.UserFormView.as_view(), name='register'),
    # ex: /diary/create/
    path('create/', views.CreateView.as_view(), name='create'),
    # ex: /diary/login
    path('login/', auth_views.LoginView.as_view()),
    # ex: /diary/settings
    path('settings/', views.settings, name='settings'),
    # ex: /diary/settings/password
    path('settings/password/', views.password, name='password'),



]
