from django.urls import path
from . import views

urlpatterns = [
    path('getpoints', views.getPoints),
    path('addpoint/', views.addPoint),
]
