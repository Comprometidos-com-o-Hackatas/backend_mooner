import mercadopago
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

sdk = mercadopago.SDK(settings.MP_ACCESS_TOKEN)

class QrCodeView(APIView):
    def post(self, request):
        payment_data = {
            "transaction_amount": 0.01,
            "description": "Descrição do produto",
            "external_reference": "ORDER1234",
            "payment_method_id": 'pix',
            "payer": {
                "email": "comprador@exemplo.com"
            }
        }

        payment = sdk.payment().create(payment_data)

        return Response(status=status.HTTP_200_OK, data={
            "id": payment['response']['id'],
            'qr_code_base64': payment['response']['point_of_interaction']['transaction_data']['qr_code_base64'],
            "qr_code": payment['response']['point_of_interaction']['transaction_data']['qr_code']
        })