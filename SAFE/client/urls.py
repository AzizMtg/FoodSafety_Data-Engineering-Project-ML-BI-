from django.urls import path
from . import views

urlpatterns = [
    path('', views.clients_list, name='clients_list'),
    path('create/<int:id>/', views.create_client, name='create_client'),
    path('update/<int:pk>/', views.update_client, name='update_client'),
    path('delete/<int:pk>/', views.delete_client, name='delete_client'),
]
