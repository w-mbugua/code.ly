from django.urls import path
from .views import ProfileListView, ProfileDetailView, my_profile, ProfileList


urlpatterns = [
    path('', ProfileListView.as_view(), name='profiles_all'),
    path('<int:pk>', ProfileDetailView.as_view(), name='profile_details'),
    path('user/<str:username>/', my_profile, name="user_profile"),
    path('api/profiles/', ProfileList.as_view())
]