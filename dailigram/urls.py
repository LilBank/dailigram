from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView
# from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.auth import views as auth_views
from diary import views


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('diary/', include('diary.urls')),
    path('', RedirectView.as_view(url='/login/')),
    path('auth/', include('social_django.urls', namespace='social')),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout')
]