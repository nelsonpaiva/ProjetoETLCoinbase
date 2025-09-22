'''
Forma mais objetiva
import requests
# Importa a biblioteca 'requests' para realizar requisições HTTP.

url = "https://jsonplaceholder.typicode.com/comments"
# Define a URL da API de teste (endpoint de comentários).

params = {"postId": 1}
# Define os parâmetros da requisição (query string: ?postId=1).

resposta = requests.get(url, params=params)
# Faz a requisição GET para a URL com os parâmetros definidos.
# Retorna um objeto Response com status, cabeçalhos e conteúdo.

comentarios = resposta.json()
# Converte o corpo da resposta (JSON) em objetos Python (lista/dicionário).

print(f"Foram encontrados {len(comentarios)} comentários.")
# Mostra a quantidade de comentários retornados pela API. Conta comentários.

print(f"Erro: {resposta.status_code} - {resposta.text}")  # Código de status HTTP
# Exibe o código de status HTTP e o corpo da resposta.
# Obs: imprime "Erro" mesmo quando a resposta for bem-sucedida (200 OK).

'''

import requests
# Importa a biblioteca 'requests', amplamente usada para fazer requisições HTTP em Python.
# Observação: 'requests' é uma biblioteca de terceiros (pip install requests). Sem ela, o import falhará.

url = "https://jsonplaceholder.typicode.com/comments"
# Define a URL do endpoint que será consultado.
# Aqui trata-se da API pública de teste "jsonplaceholder" que retorna comentários em JSON.

params = {"postId": 1}
# Dicionário com parâmetros de consulta (query string) que serão enviados junto com a requisição GET.
# requests irá transformar isso em '?postId=1' na URL final.
# Usar params evita concatenar strings manualmente e cuida da codificação adequada.

resposta = requests.get(url, params=params)
# Executa a requisição HTTP GET para a URL com os parâmetros definidos.
# Retorna um objeto 'Response' contendo:
# - resposta.status_code (código HTTP)
# - resposta.headers (cabecalhos HTTP)
# - resposta.text (corpo como string)
# - resposta.content (corpo em bytes)
# - resposta.json() (conversão do corpo para Python, se for JSON)
# **Atenção / Boas práticas**:
#  - Sem timeout: a chamada pode travar indefinidamente se o servidor não responder.
#    Prefira: requests.get(url, params=params, timeout=5)
#  - A chamada pode levantar exceções (ConnectionError, Timeout, RequestException).
#    Em produção, envolva em try/except para tratar falhas de rede.

comentarios = resposta.json()
# Converte o corpo da resposta (assumindo JSON) em objetos Python (normalmente lista/dicionário).
# Possíveis problemas:
# - Se o corpo não for JSON válido, .json() levantará uma exceção (ValueError / JSONDecodeError).
# - Chamá-lo sem checar o status pode levar a exceções ou a parsing de mensagens de erro HTML.
# Recomendações:
# - Verificar resposta.ok ou resposta.status_code antes de usar .json()
# - Envolver a conversão em try/except para tratar payloads inválidos.

print(f"Foram encontrados {len(comentarios)} comentários.")
# Imprime quantos comentários foram retornados, usando len() (assume-se que 'comentarios' é uma lista).
# Possíveis problemas:
# - Se 'comentarios' não for iterável (p.ex. None ou dict), len() pode lançar TypeError.
# - Melhor validar o tipo antes: if isinstance(comentarios, list): ...

print(f"Erro: {resposta.status_code} - {resposta.text}")  # Código de status HTTP
# Imprime o código de status HTTP e o corpo em texto da resposta.
# Observações importantes:
# - Rotular essa linha como "Erro" é enganoso quando o status_code for 200 (sucesso).
# - Em vez disso, condicione a mensagem a respostas de erro:
#     if not resposta.ok:
#         print(...)
# - resposta.text pode ser muito grande (cuidado ao imprimir logs).
# - Para lançar exceções automáticas em 4xx/5xx: resposta.raise_for_status()