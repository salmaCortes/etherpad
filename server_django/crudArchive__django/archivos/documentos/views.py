from rest_framework import viewsets, status
from rest_framework.response import Response
import requests

class DocViewSet(viewsets.ViewSet):

    def create(self, request):
        # Obtener el nombre del pad desde la solicitud
        pad_name = request.data.get('padName')

        if not pad_name:
            return Response({"error": "padName is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        etherpad_base_url = 'http://localhost:9001/api/1/'
        api_key = '88cd01a8205f9dd910125770de87f274365cc21d52bf0709d56f80c171350d05'
        url = f'{etherpad_base_url}createPad?padID={pad_name}&apikey={api_key}'

        try:
            # Realizar la solicitud POST a Etherpad
            response = requests.post(url)
            response_data = response.json()  # Convertir la respuesta de Etherpad a JSON
            if response.status_code == 200:
                return Response({
                    "message": "Documento y pad creados exitosamente",
                    "padName": pad_name
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    "message": "Documento creado pero error al crear el pad en Etherpad",
                    "details": response_data
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({
                "message": "Documento creado pero error al comunicarse con Etherpad",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Otros métodos (retrieve, update, delete, list, etc.) pueden ir aquí si es necesario
