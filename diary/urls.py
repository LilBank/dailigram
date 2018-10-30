from django.urls import path,  include
from diary import views
from django.contrib.auth import views as auth_views

app_name = 'diary'
urlpatterns = [

    path('', views.index, name='index'),
    # ex: /diary/register/
    # path('register/', views.UserFormView.as_view(), name = 'register'),
    # ex: /diary/create/
    path('create/', views.create, name='create'),
]
