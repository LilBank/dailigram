from django.urls import path
from diary import views

app_name = 'diary'
urlpatterns = [
    # ex: /diary/
    path('', views.index, name='index'),

    # ex: /diary/create/
    path('create/', views.create, name='create'),

]
