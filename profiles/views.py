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

def my_profile(request, username): 
    username = request.user.username
    profile = Profile.objects.filter(user__username=username)
    print("**********************")
    print('PROFILE:',profile)
    return render(request, 'profiles/user_profile.html', {'user_profile': profile})