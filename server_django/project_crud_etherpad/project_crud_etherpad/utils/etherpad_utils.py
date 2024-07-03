
import requests

def create_pad(pad_name):
    etherpad_base_url = 'http://localhost:9001/api/1/'
    api_key = '88cd01a8205f9dd910125770de87f274365cc21d52bf0709d56f80c171350d05'

    url = f'{etherpad_base_url}createPad?padID={pad_name}&apikey={api_key}'

    response = requests.post(url)
    return response.json()
