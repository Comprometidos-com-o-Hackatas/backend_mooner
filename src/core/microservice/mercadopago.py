import mercadopago
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.usuario.models import Usuario as User

sdk = mercadopago.SDK(settings.MP_ACCESS_TOKEN)

class AssignView(APIView):
    def post(self, request):
        email = request.data.get('formData')['payer']['email']
        user = User.objects.get(email=email)
        
        try:
            user.premium = request.data.get('description')
            user.save()
            return Response(status=status.HTTP_200_OK, data={'msg': 'se prepare para navegar num universo além da lua, com o mooner premium!!!'})
        except user.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'err': 'dados inválidos'})


