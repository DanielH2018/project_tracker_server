from rest_api.models import Project, ProjectMembership, Task
from rest_framework import serializers
from django.contrib.auth.models import User
from django.db import models

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username']

class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username', required=False)

    class Meta:
        model = Project
        fields = ('__all__')

    # Create a Project Membership with maximum permissions on Project creation
    def create(self, validated_data):
        project = super().create(validated_data=validated_data)
        ProjectMembership.objects.create(owner=self.context['request'].user, project=project, permission_level=1)
        return project

class ProjectMembershipSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username', required=False)
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())

    class Meta:
        model = ProjectMembership
        fields = ('__all__')

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username', required=False)
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())

    class Meta:
        model = Task
        fields = ('__all__')        

