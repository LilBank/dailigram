from django.urls import path
from diary import views

app_name =  'diary'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('register/', views.UserFormView.as_view(), name = 'register'),
]