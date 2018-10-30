from django.urls import path
from diary import views

app_name = 'diary'
urlpatterns = [
    # ex: /diary/
    path('', views.index, name='index'),
    # ex: /diary/register/
    # path('register/', views.UserFormView.as_view(), name = 'register'),
    # ex: /diary/create/
    path('create/', views.create, name='create'),
    # ex: /diary/login
    # path('login/', views.LoginView, name = 'login'),

]
