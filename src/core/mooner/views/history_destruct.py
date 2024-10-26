from ..models import History
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class HistoryDestroyView(APIView):
    def delete(self, request, *args, **kwargs):
        user = request.user
        History.objects.filter(usuario=user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data={'msg': 'historico deletado'})