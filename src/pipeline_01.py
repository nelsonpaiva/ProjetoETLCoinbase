import time
import requests  # Importa a biblioteca requests para fazer requisições HTTP
from tinydb import TinyDB  # Importa a classe TinyDB da biblioteca tinydb para manipulação de banco de dados NoSQL
from datetime import datetime  # Importa a classe datetime para manipulação de datas e horas

# Função para extrair os dados do preço do Bitcoin via API do Coinbase
def extract_dados_bitcoin():
    url = "https://api.coinbase.com/v2/prices/spot"  # Define a URL do endpoint para obter o preço spot do Bitcoin
    response = requests.get(url)  # Realiza uma requisição GET para a URL definida
    dados = response.json()       # Converte a resposta da requisição para um dicionário Python usando o método json()
    return dados                  # Retorna o dicionário com os dados extraídos

# Função para transformar os dados extraídos em um formato mais simples
def transform_dados_bitcoin(dados):
    valor = dados['data']['amount']        # Extrai o valor do Bitcoin dos dados retornados
    criptomoeda = dados['data']['base']    # Extrai o nome da criptomoeda (ex: 'BTC')
    moeda = dados['data']['currency'] # Extrai a moeda de referência (ex: 'USD')
    timestamp = datetime.now().timestamp()  # Extrai o timestamp atual no formato ISO 8601
          
    dados_transformados = {                # Cria um novo dicionário apenas com as informações relevantes
        'valor': valor,
        'criptomoeda': criptomoeda,
        'moeda': moeda ,
        'timestamp': timestamp
    }
    return dados_transformados              # Retorna o dicionário transformado

def salvar_dados_tinydb(dados, db_name = "bitcoin.json"): #passando os dados para a função salvar. Esses dados são do dados_transformados. Depois passo o nome do meu banco de dados
# ele vai criar um arquivo local do tipo json 
    db = TinyDB(db_name) #agora falo que meu banco de dados vai ser do tipo TinyDB e passo o nome do banco de dados
    db.insert(dados) #insere os dados no banco de dados que passei na função acima
    print(f"Dados salvos no banco de dados {db_name}") #printa uma mensagem dizendo que os dados foram salvos no banco de dados


# Bloco de execução principal do script
if __name__ == "__main__":                  # Verifica se o script está sendo executado diretamente
    
    while True:
        dados_json = extract_dados_bitcoin()         # Chama a função para extrair os dados do Bitcoin
        dados_tratados = transform_dados_bitcoin(dados_json)  # Chama a função para transformar os dados extraídos
        #print(dados_tratados)              # Exibe os dados transformados no terminal
        salvar_dados_tinydb(dados_tratados)  # Chama a função para salvar os dados no banco de dados
        time.sleep(15)  # Aguarda 15 segundos antes de repetir o processo
        
