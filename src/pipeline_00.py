import requests

#Agora vamos transformar o trecho abaixo em uma função do bitcoin

def extract_dados_bitcoin():
    #vamos pegar a ulr do spot price
    url = "https://api.coinbase.com/v2/prices/spot"

    # depois da URL eu quero pegar o response
    response = requests.get(url)

    #depois vou pegar os meus dados usando o método json
    #importante pois vai transformar o response em um dicionário, sem headers e outras informações
    #se eu quisesse o header usaria response.headers,
    dados = response.json() 

    return dados

def transform_dados_bitcoin(dados):
    valor = dados['data']['amount']
    criptomoeda = dados['data']['base']
    moeda = dados['data']['currency']

    # a partir disso quero que salve dentro de uma chave dados_transformados
    # e dentro dessa chave quero que tenha o valor, a criptomoeda e a moeda
    # E depois salvar isso tudo em um banco de dadosq
    dados_transformados = {
        'valor': valor,
        'criptomoeda': criptomoeda,
        'moeda': moeda  
    }
    return dados_transformados

#por fim vou printar os dados

#por fim vou printar os dados

if __name__ == "__main__":
    #extrair os dados
    dados = extract_dados_bitcoin()
    dados_transformados = transform_dados_bitcoin(dados)
    print(dados_transformados)