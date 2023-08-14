from rest_framework import serializers
from projetos.models import Projetos
from users.models import Profile

class ProjetosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projetos
        fields = '__all__'
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['name', 'username', 'email', 'user', 'created']