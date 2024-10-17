from rest_framework.serializers import ModelSerializer, SlugRelatedField
from django.contrib.auth.hashers import make_password
from .models import Usuario, Collaborator


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)
    
class CollaboratorSerializer(ModelSerializer):
    class Meta:
        model = Collaborator
        fields = "__all__"
    
    