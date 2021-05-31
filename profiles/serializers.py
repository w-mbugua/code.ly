from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    model = Profile
    fields = '__all__'