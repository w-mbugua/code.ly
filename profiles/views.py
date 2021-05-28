from profiles.models import Profile
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Profile

class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        return Profile.objects.all().exclude(user=self.request.user)

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_details.html'
