from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-course/', views.add_course, name='add_course'),
    path('view-courses/', views.view_courses, name='view_courses'),
    path('edit-course/<int:id>/', views.edit_course, name='edit_course'),
    path('delete-course/<int:id>/', views.delete_course, name='delete_course'),
]