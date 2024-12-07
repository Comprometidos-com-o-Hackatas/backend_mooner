from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import mercadopago 
from django.conf import settings
sdk = mercadopago.SDK(settings.MP_ACCESS_TOKEN)

class WebHookView(APIView):
    def post(self, request):
        try: 
            payment_data = request.data.get('data', {})
            payment_id = payment_data.get('id')
            user_payment = sdk.payment().get(payment_id)
            payment_reponse = user_payment.get('response', {})
            payment_status = payment_reponse.get("status")

            print(payment_status)

            return Response(status=status.HTTP_200_OK, data={'status': payment_id})
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'status': str(e)})