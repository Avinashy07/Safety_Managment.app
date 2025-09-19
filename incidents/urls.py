# incidents/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.incident_list, name='incident_list'),
    path('incident/new/', views.incident_create, name='incident_create'),
    path('incident/<int:pk>/edit/', views.incident_update, name='incident_update'),
    path('incident/<int:pk>/delete/', views.incident_delete, name='incident_delete'),
]