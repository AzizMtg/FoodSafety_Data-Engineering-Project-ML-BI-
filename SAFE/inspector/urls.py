from django.urls import path
from . import views

urlpatterns = [
    path('', views.inspections_list, name='inspections_list'),
    path('create/', views.create_inspection, name='create_inspection'),
    path('update/<int:pk>/', views.update_inspection, name='update_inspection'),
    path('delete/<int:pk>/', views.delete_inspection, name='delete_inspection'),
    path('facility/<int:pk>/', views.facility_insp, name='facility_insp'),  # Add this line

]
