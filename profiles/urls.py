from django.urls import path
from .views import ProfileListView, ProfileDetailView
urlpatterns = [
    path('', ProfileListView.as_view(), name='profiles_all'),
    path('<int:pk>', ProfileDetailView.as_view(), name='profile_details')
]