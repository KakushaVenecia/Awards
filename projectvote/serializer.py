from rest_framework import serializers
from .models import Profile, Project

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile_pic', 'name', 'bio', 'location')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('photo', 'name', 'description')

    