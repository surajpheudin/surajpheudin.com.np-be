from django.urls import path

from . import views

urlpatterns = [
    path('<str:pk>/', views.GetProjects.as_view()),
]
