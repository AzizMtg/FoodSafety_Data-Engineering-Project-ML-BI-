from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profileInspector/', views.profileInspector, name='profileInspector'),
    path('profileClient/', views.profileClient, name='profileClient'),
    path('profileOwner/', views.profileOwner, name='profileOwner'),
    path('dashboard/', views.dashboard_redirect, name='dashboard'),  # Redirect based on the user role
]
