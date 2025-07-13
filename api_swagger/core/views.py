from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class HelloView(APIView):
    @swagger_auto_schema(
        operation_description="Devuelve un saludo",
        responses={200: openapi.Response('Respuesta exitosa')}
    )
    def get(self, request):
        """
        Endpoint que devuelve un mensaje de saludo
        """
        return Response({'mensaje': '¡Hola desde la API!'}, status=status.HTTP_200_OK)
