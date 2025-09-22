import requests
# Importa a biblioteca 'requests' para realizar requisições HTTP.

url = "https://jsonplaceholder.typicode.com/comments"
# Define a URL da API de teste (endpoint de comentários).

params = {"postId": 1}
# Define os parâmetros da requisição (query string: ?postId=1).

resposta = requests.get(url, params=params, headers={"User-Agent": "Mozilla/5.0"})
# Faz a requisição GET para a URL com os parâmetros definidos.
# Retorna um objeto Response com status, cabeçalhos e conteúdo.

comentarios = resposta.json()
# Converte o corpo da resposta (JSON) em objetos Python (lista/dicionário).

print(f"Foram encontrados {len(comentarios)} comentários.")
# Mostra a quantidade de comentários retornados pela API. Conta comentários.

print(f"Erro: {resposta.status_code} - {resposta.text}")  # Código de status HTTP
# Exibe o código de status HTTP e o corpo da resposta.
# Obs: imprime "Erro" mesmo quando a resposta for bem-sucedida (200 OK).
