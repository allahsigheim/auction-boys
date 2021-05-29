from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='land'),
    path('<int:land_id>/', views.detail, name='detail'),
]