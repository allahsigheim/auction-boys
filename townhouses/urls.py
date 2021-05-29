from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='townhouses'),
    path('<int:townhouses_id>/', views.detail, name='detail'),
]