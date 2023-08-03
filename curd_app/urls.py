from django.urls import path
from .views import ProjectAPI, ProjectDetailsAPI

urlpatterns = [
    path('project/', ProjectAPI.as_view()),
    path('project/<int:pk>/', ProjectDetailsAPI.as_view()),
]
