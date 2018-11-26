from django.urls import path
from diary import views
from django.contrib.auth.decorators import login_required

app_name = 'diary'
urlpatterns = [
    path('register/', views.UserFormView.as_view(), name='register'),
    path('', login_required(views.IndexView.as_view()), name='index'),
    path('create_page/', login_required(views.CreatePage.as_view()), name='create_page'),
    path('format/', login_required(views.Format.as_view()), name='format'),
    path('layout_1/', login_required(views.Layout_1.as_view()), name='layout_1'),
    # path('layout_2/', login_required(views.CreateFormat.as_view()), name='layout_2'),
    # path('layout_3/', login_required(views.CreateFormat.as_view()), name='layout_3'),
    path('settings/', login_required(views.Settings.as_view()), name='settings'),    
    path('<int:pk>/', login_required(views.DetailView.as_view()), name='detail'),
    path('<int:pk>/delete/', login_required(views.DeleteDiary.as_view()), name='delete_diary')

]