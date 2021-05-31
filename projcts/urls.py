from django.urls import path
from .views import (
    ProjectListView,
    ProjectDetailView,
    ProjectEditView,
    ProjectDeleteView,
    ProjectCreateView,
    ReviewCreateView,
    project_search,
)

urlpatterns = [
    path('', ProjectListView.as_view(), name="project_list"),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name="project_details"),
    path('projects/<int:pk>/edit/', ProjectEditView.as_view(), name="project_edit"),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name="project_delete"),
    path('projects/new/', ProjectCreateView.as_view(), name="new_project"),
    path('projects/<int:pk>/review/', ReviewCreateView.as_view(), name="newreview"),
    path('search/', project_search, name="search"),
]