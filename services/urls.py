from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.services, name='services'),
    path('add/',views.add_service, name='add_service'),
    path('edit/<int:id>/',views.edit_service, name='edit_service'),
    path('delete/<int:id>/',views.delete_service, name='delete_service'),
    
    
    # Testimonial URLs
    path('testimonials/', views.view_testimonials, name='view_testimonials'),
    path('testimonials/add/', views.add_testimonial, name='add_testimonial'),
    path('testimonials/edit/<int:id>/', views.edit_testimonial, name='edit_testimonial'),
    path('testimonials/delete/<int:id>/', views.delete_testimonial, name='delete_testimonial'),
    
    
]