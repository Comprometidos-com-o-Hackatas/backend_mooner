import mercadopago
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.usuario.models import Usuario as User

sdk = mercadopago.SDK(settings.MP_ACCESS_TOKEN)

class AssignView(APIView):
    def post(self, request, email):
        print(request.data['formData'])
        try:
            user = User.objects.get(email=email)

            payment = request.data['formData']

            payment_response = sdk.payment().create(payment)

            print('printou', payment_response)
            
            if 'response' in payment_response:
                payment = payment_response.get("response")

                if payment_response.get("status") == 201:
                    user.premium = request.data.get('description')
                    user.save()
                    return Response(status=status.HTTP_200_OK, data={'msg': 'se prepare para navegar num universo além da lua, com o mooner premium!!!'})
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'err': 'Pagamento não aprovado'})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'err': 'Chave "response" não encontrada na resposta do pagamento'})

        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'err': 'Usuário não encontrado'})
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'err': str(e)})

    def get(self, request, email):
        try:
            user = User.objects.get(email=email)
            payment_data = {
                "transaction_amount": 0.01,
                "description": "Pagamento via PIX",
                "payment_method_id": "pix",
                "payer": {
                    "email": email,
                    "first_name": 'luan',
                    "last_name": 'silva',
                    "identification": {
                        "type": "CPF",
                        "number": "13980382966"
                    }
                },
            }

            payment_response = sdk.payment().create(payment_data)
            payment = payment_response.get("response")
            return Response(status=status.HTTP_200_OK, data={
                        "qr_code": payment["point_of_interaction"]["transaction_data"]["qr_code"],
                        "qr_code_base64": payment["point_of_interaction"]["transaction_data"]["qr_code_base64"]
                    })
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'err': 'Usuário não encontrado'})
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'err': str(e)})
