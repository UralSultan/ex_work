from django.contrib import admin
from django.urls import path
from guest_book import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.guest_list, name="guest_list"),
    path('add/', views.guest_add, name='guest_add'),
    path('guest/<int:pk>/update/', views.guest_update, name='guest_update'),
]