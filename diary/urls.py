from django.urls import path,  include
from diary import views

app_name = 'diary'
urlpatterns = [
    # ex: /diary/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /diary/register/
    path('register/', views.UserFormView.as_view(), name='register'),
    # ex: /diary/create/
    path('create/', views.CreateView.as_view(), name='create'),
    # ex: /diary/login
    path('login/', views.LoginView.as_view(), name='login'),
    # ex: /diary/settings
    path('settings/', views.SettingsView.as_view(), name='settings'),
    # ex: /diary/settings/password
    path('settings/password/', views.PasswordView.as_view(), name='password'),



]
