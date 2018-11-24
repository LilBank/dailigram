from django.urls import path
from diary import views
from django.contrib.auth.decorators import login_required

app_name = 'diary'
urlpatterns = [
    path('register/', views.UserFormView.as_view(), name='register'),
    path('', login_required(views.IndexView.as_view()), name='index'),
    # ex: /diary/create_page1/
    path('create_page1/', login_required(views.CreatePage1.as_view()), name='create_page1'),
    # ex: /diary/create_page2/
    path('create_page2/', login_required(views.CreatePage2.as_view()), name='create_page2'),
    # ex: /diary/create_page3/
    path('create_page3/', login_required(views.CreatePage3.as_view()), name='create_page3'),
    # ex: /diary/format/
    path('format/', login_required(views.CreateFormat.as_view()), name='format'),
    path('<int:pk>/', login_required(views.DetailView.as_view()), name='detail'),
    # ex: /diary/detail(2)/delete/
    path('<int:pk>/delete/', login_required(views.DeleteDiary.as_view()), name='delete_diary'),
     # ex: /diary/settings/
    path('settings/', login_required(views.CreateSettings.as_view()), name='settings')

]
