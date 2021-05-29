from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='houses'),
    path('<int:house_id>/', views.detail, name='detail'),
]