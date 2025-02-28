from django.contrib import admin
from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.login, name ='login'),
    path('add_project/', views.add_project , name='add_project'),
    path('edit_project/', views.edit_project , name="edit_project"),
    path('projects/' , views.project_listing , name="projects"),
    path('project_details/<int:id>/' , views.project_details , name='project_details'),
    path('register/' , views.register , name='register'),
    path('about/' , views.about , name='about'),
    path('contact/' , views.contact , name='contact'),
    path('home/' , views.home , name='home'),
    path('logout/' , views.user_logout , name="logout"),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('thanks/' , views.ThankYou , name="thanks"),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
]