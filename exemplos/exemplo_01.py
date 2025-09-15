import requests

url = 'https://www.google.com/'

#depois verificar os métodos na sequência da biblioteca
# seguir o mapa mental após biblioteca requests
# Se o navegador consegue essas informações pelo:
# GET: pede um recurso ao sercidor (select * from)
# POST: Envia dados para o servidor (insert into)
# PUT: Criar ou Atualiza dados no servidor (update)
# DELETE: Deleta dados no servidor (delete from)

# Minha biblioteca vai fazer um request, vai pedir alguma coisa e vai voltar um resposta da minha API

#método GET
#resposta = requests.get(url)#único parâmetro obrigatório é a URL

#print(resposta)#depois trazer a resposta

#depois salvo e executar no terminal
# para roda o terminal: python exemplos/exemplo_01.py
# O resultado é: <Response [200]>  (código de status HTTP)

# Olhando o mapa mental, pela família de retorno o código 200 é da família 2xx, que é sucesso

#método POST
resposta = requests.post(url)

print(resposta)
# O resultado é: <Response [405]>  (código de status HTTP)
# Olhando o mapa mental, pela família de retorno o código 405 é da família 4xx, que é erro do cliente
# Família do 4xx: erro do cliente

# Famíla do 5xx: erro do servidor

