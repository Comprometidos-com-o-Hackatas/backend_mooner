from ..models import Artist, Usuario
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from ..serializers import ArtistCreateSerializer, ArtistSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from utils.artist_filter import ArtistFilter


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ArtistFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return ArtistCreateSerializer
        return ArtistSerializer

@api_view(['GET'])
def verify_email(req, verification_token):
    try:
        user = Usuario.objects.get(token_verification=verification_token)
    except ValueError as e:
        return Response({'error': f'Token de verificação inválido {e}'}, status=status.HTTP_404_NOT_FOUND)

    user.is_artist = True
    user.token_verification = None 
    user.save()

    return Response({'message': 'Usuário verificado com sucesso, volte para o site'}, status=status.HTTP_200_OK)