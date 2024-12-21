# owner/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.facilities_list, name='facilities_list'),  # Make sure this is named 'facilities_list'
    path('create/', views.create_facility, name='create_facility'),
    path('update/<int:pk>/', views.update_facility, name='update_facility'),
    path('delete/<int:pk>/', views.delete_facility, name='delete_facility'),
    path('<int:id>/', views.facility_detail, name='facility_detail'),
        path('predict_revenue/<int:pk>/', views.predicter_Revenue, name='predict_revenue'),
]
