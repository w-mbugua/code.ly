from rest_framework import serializers
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required

from .models import Profile
from .serializer import ProfileSerializer

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profiles/profile_details.html'

class ProfileEditView(UpdateView):
    model = Profile
    fields = '__all__'
    template_name = 'profiles/profile_edit.html'

class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        return Profile.objects.all().exclude(user=self.request.user)

@login_required
def my_profile(request, username): 
    username = request.user.username
    profile = Profile.objects.filter(user__username=username)
    print("**********************")
    print('PROFILE:',profile)
    return render(request, 'profiles/user_profile.html', {'user_profile': profile})

class ProfileList(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializers = ProfileSerializer(profiles, many=True)
        return Response(serializers.data)
