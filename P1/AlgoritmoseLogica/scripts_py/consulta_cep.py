import requests
from pprint import pprint

cep = int(input('Informe o cep que deseja consultar: '))
url = f'https://viacep.com.br/ws/{cep}/json/'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    pprint(data)
else:
    print(f'Erro: {response.status_code}')