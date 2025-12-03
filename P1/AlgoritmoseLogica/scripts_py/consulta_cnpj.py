import requests
from pprint import pprint

moeda = input('Informe a moeda: ')
data = input('Informe a data (YYYY-MM-DD): ')
url = f"https://brasilapi.com.br/api/cambio/v1/cotacao/{moeda}/{data}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    pprint(data)

else:
    print(f'Erro: {response.status_code}')