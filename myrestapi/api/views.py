from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ProjetosSerializer
from .serializers import ProfileSerializer
from projetos.models import Projetos
from users.models import Profile


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': 'api/projetos'},
        {'GET': 'api/perfil'},
        {'POST': 'api/users/token'},
        
    ]
    return Response(routes)

@api_view(['GET'])
def getProjetos(request):
    projetos = Projetos.objects.all()
    serialize = ProjetosSerializer(projetos, many = True)
    print(serialize.data)
    
    return Response(serialize.data)

@api_view(['GET'])
def getProfile(request):
    projetos = Profile.objects.all()
    serialize = ProfileSerializer(projetos, many = True)
    print(serialize.data)
    
    return Response(serialize.data)

