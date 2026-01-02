from rest_framework import serializers
from .models import Item
from django.contrib.auth.models import User
    
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'  # This includes id, name, shape, color, created_at
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # This "automates" the password hashing
        user = User.objects.create_user(**validated_data)
        return user