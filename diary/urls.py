from django.urls import path ,  include
from diary import views

app_name =  'diary'
urlpatterns = [
     # ex: /diary/
    path('', views.IndexView.as_view(), name='index'),
     # ex: /diary/register/
    path('register/', views.UserFormView.as_view(), name = 'register'),
     # ex: /diary/create/    
    path('create/', views.CreateView.as_view(), name = 'create'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('auth/',include('social_django.urls', namespace='social')),  # <- Here

]