import mercadopago
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.usuario.models import Usuario as User
sdk = mercadopago.SDK(settings.MP_ACCESS_TOKEN)

class PaymentStatusView(APIView):
    def get(self, request, id, user, plan):
            user_email = User.objects.get(email=user) 
            payment = sdk.payment().get(id)
            payment_status = payment['response']['status']
            print(payment_status)
            if payment_status == 'approved':
                user_email.premium = plan
                user_email.save()
                return Response(status=status.HTTP_200_OK, data={'msg': 'se prepare para navegar num universo além da lua, com o mooner premium!!!'})
            else:
                return Response(status=status.HTTP_202_ACCEPTED, data={'status': payment_status})