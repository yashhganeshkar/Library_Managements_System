
from . import views
from django.urls import path

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path("details/<int:book_id>", views.book_details, name='book_details'),
    path('create/', views.book_create, name='book_create'),
    path('<int:book_id>/delete/', views.book_delete, name='book_delete'),
    path('<int:book_id>/edit/', views.book_edit, name='book_edit'),
    path('register/', views.register, name='register'),
]    