from django.urls import path,  include
from diary import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, permission_required

app_name = 'diary'
urlpatterns = [

    # ex: /diary/
    path('',login_required(views.IndexView.as_view()), name='index'),
    # ex: /diary/detail/
    path('<int:pk>/',login_required(views.DetailView.as_view()), name='detail'),
    # ex: /diary/register/
    path('register/', views.UserFormView.as_view(), name='register'),
    # ex: /diary/create/
    path('create/', views.create_diary, name='create'),
    # ex: /diary/format/
    path('format/', views.CreateFormat.as_view(), name='format')

]
