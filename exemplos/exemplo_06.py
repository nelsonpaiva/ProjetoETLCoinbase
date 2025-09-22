import requests   # Importa a biblioteca 'requests', usada para enviar requisições HTTP (GET, POST, etc.)
import json       # Importa a biblioteca 'json', usada para manipular dados em formato JSON (conversão entre dict e string)

# Define a URL do endpoint da API da OpenAI responsável por gerar respostas de chat.
# Esse endpoint recebe uma mensagem e retorna a resposta gerada pelo modelo de IA.
url = 'https://api.openai.com/v1/chat/completions'

# Define os cabeçalhos da requisição HTTP.
# - 'Content-Type': indica que o corpo da requisição será enviado no formato JSON.
# - 'Authorization': contém a chave da API (Bearer Token), necessária para autenticação.
headers = {
    'Content-Type': 'application/json',
    "Authorization": "Bearer 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"  
    # Substituir <SUA_CHAVE_API> pela chave real fornecida pela OpenAI.
}

# Define o corpo da requisição (payload), que será enviado para a API.
# Aqui informamos:
# - "model": o modelo de IA que deve ser usado (neste caso, "gpt-3.5-turbo").
# - "messages": lista de mensagens trocadas na conversa. Cada mensagem tem:
#     - "role": o papel do autor da mensagem ("user", "system" ou "assistant").
#     - "content": o texto da mensagem enviada.
# Obs.: As opções "max_tokens" e "temperature" estão comentadas, mas podem ser usadas para controlar
#       o tamanho máximo da resposta e o nível de criatividade da IA, respectivamente.
data = {
    "model": "gpt-3.5-turbo",  # Modelo de linguagem usado para processar o prompt.
    "messages": [
        {"role": "user", "content": "Qual é a capital da França?"}  # Prompt enviado pelo usuário.
    ]
    # "max_tokens": 100,     # (opcional) número máximo de tokens que a resposta pode conter.
    # "temperature": 0.7     # (opcional) controla a criatividade: 0 = respostas mais previsíveis, 1 = mais criativas.
}

# Envia a requisição POST para a API.
# - url: o endpoint da API.
# - headers: cabeçalhos de autenticação e tipo de conteúdo.
# - data: converte o dicionário 'data' em uma string JSON usando json.dumps, pois a API espera um corpo em formato JSON.
response = requests.post(url, headers=headers, data=json.dumps(data))

# Se quisermos ver a resposta completa da API (que vem em JSON),
# podemos usar: print(response.json())
# Essa resposta contém vários metadados além do texto gerado, como uso de tokens, ID da requisição etc.
# print(response.json())

# Aqui, acessamos apenas a parte da resposta que contém o texto da IA.
# - response.json() converte o corpo da resposta para um dicionário Python.
# - ['choices'][0] pega a primeira escolha de resposta gerada pelo modelo (a API pode retornar várias opções).
# - ['message']['content'] acessa o conteúdo textual da resposta.
print(response.json()['choices'][0]['message']['content'])
