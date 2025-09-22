import requests
# Importa a biblioteca 'requests' para realizar requisições HTTP.

url = "https://api.coinbase.com/v2/prices/spot"
# Define o endpoint da API do Coinbase para obter o preço atual (spot).

headers = {
    "Accept": "application/json",
    "User-Agent": "MinhaAplicacao/1.0"
}
# Define os cabeçalhos HTTP: tipo de resposta esperado (JSON) e identificação da aplicação.

params = {"currency": "USD"}  # moeda de consulta
# Parâmetros da requisição: aqui consulta o preço em dólares (USD).

resposta = requests.get(url, headers=headers, params=params)
# Faz a requisição GET para a API, enviando cabeçalhos e parâmetros.

data = resposta.json()
# Converte a resposta JSON em objeto Python (dicionário).

print("Preço do Bitcoin (BTC) em USD:", data["data"]["amount"])
# Exibe o valor atual do Bitcoin em USD, acessando a chave correta no JSON.

