import requests
from pprint import pprint

cnpj = int(input('Informe o CNPJ: '))
url = f"https://publica.cnpj.ws/cnpj/{cnpj}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    pprint(data)
else:
    print(f'Erro: {response.status_code}')