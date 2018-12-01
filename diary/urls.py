from django.urls import path
from diary import views
from django.contrib.auth.decorators import login_required

app_name = 'diary'
urlpatterns = [
    path('register/', views.UserFormView.as_view(), name='register'),
    path('', login_required(views.IndexView.as_view()), name='index'),
    path('create_page/', login_required(views.CreatePage.as_view()), name='create_page'),
    path('format/', login_required(views.Format.as_view()), name='format'),    
    path('<int:pk>/', login_required(views.DetailView.as_view()), name='detail'),
    path('<int:pk>/delete/', login_required(views.DeleteDiary.as_view()), name='delete_diary')

]