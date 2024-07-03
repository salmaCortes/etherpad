# views.py en tu aplicación Django
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests

@csrf_exempt
def create_pad(request):
    if request.method == 'POST':
        pad_name = request.POST.get('padName')  # Obtén el nombre del pad desde React

        # Configura la llamada a Etherpad
        etherpad_base_url = 'http://localhost:9001/api/1/'
        api_key = '88cd01a8205f9dd910125770de87f274365cc21d52bf0709d56f80c171350d05'

        url = f'{etherpad_base_url}createPad?padID={pad_name}&apikey={api_key}'

        try:
            # Realiza la solicitud POST a Etherpad
            response = requests.post(url)
            response_data = response.json()  # Convierte la respuesta de Etherpad a JSON
            return JsonResponse(response_data)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
