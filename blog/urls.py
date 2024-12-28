from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('test/', views.check_session, name='check_session'),
    path('logout/',views.logout, name='logout'),
    path('post/<int:id>', views.post_detail, name = 'post_detail')
]