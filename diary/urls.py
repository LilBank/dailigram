from django.urls import path,  include
from diary import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, permission_required

app_name = 'diary'
urlpatterns = [

    # ex: /diary/register/
    path('register/', views.UserFormView.as_view(), name='register'),
    # ex: /diary/
    path('', login_required(views.IndexView.as_view()), name='index'),
    # ex: /diary/create_diary/
    path('create_diary/', login_required(views.CreateDiary.as_view()),name='create_diary'),
    # ex: /diary/create_page/
    path('create_page/', login_required(views.CreatePage.as_view()), name='create_page'),
    # ex: /diary/format/
    path('format/', login_required(views.CreateFormat.as_view()), name='format'),
     # ex: /diary/detail(1)/
    path('<int:pk>/', login_required(views.DetailView.as_view()), name='detail'),
    # ex: /diary/detail(2)/delete/
    path('<int:pk>/delete/', login_required(views.DeleteDiary.as_view()), name='delete_diary')

]
