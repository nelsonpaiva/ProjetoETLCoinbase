import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

resposta = requests.get(url)
data = resposta.json()

print(data)
#trás o resultado:
#{'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit...
# ou seja, trás a mesma informação da url do navegador, mas sem ter que renderizar a página, apenas com o request

# Esse Json nada mais é que uma planilha, uma tabela, um dicionário com várias chaves e valores.