import os  # Importa o módulo os para acessar variáveis de ambiente do sistema operacional
import time  # Importa o módulo time para usar funções de tempo (ex: sleep)
import requests  # Importa a biblioteca requests para fazer requisições HTTP
from datetime import datetime  # Importa a classe datetime para manipular datas e horários
from dotenv import load_dotenv  # Importa a função para carregar variáveis de ambiente do arquivo .env
from sqlalchemy import create_engine  # Importa a função para criar a engine de conexão com o banco de dados
from sqlalchemy.orm import sessionmaker  # Importa o sessionmaker para criar sessões de banco de dados

# Importar Base e BitcoinPreco do database.py (modelos do banco de dados)
from database import Base, BitcoinPreco

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Lê as variáveis separadas do arquivo .env (sem SSL)
POSTGRES_USER = os.getenv("POSTGRES_USER")         # Lê o usuário do banco de dados
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD") # Lê a senha do banco de dados
POSTGRES_HOST = os.getenv("POSTGRES_HOST")         # Lê o host do banco de dados
POSTGRES_PORT = os.getenv("POSTGRES_PORT")         # Lê a porta do banco de dados
POSTGRES_DB = os.getenv("POSTGRES_DB")             # Lê o nome do banco de dados

#comando para verificar se tem algum erro nas variáveis de ambiente
#print("USER:", POSTGRES_USER)
#print("PASSWORD:", POSTGRES_PASSWORD)
#print("DB:", POSTGRES_DB)
#print("HOST:", POSTGRES_HOST)
#print("PORTA:", POSTGRES_PORT)

# Monta a URL de conexão ao banco PostgreSQL (sem ?sslmode=...)
DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)
#print("DATABASE_URL:", DATABASE_URL)  # verifica se a URL está correta

#print("PORTA:", POSTGRES_PORT)

# Cria o engine e a sessão
engine = create_engine(DATABASE_URL)  # Cria a engine de conexão com o banco de dados
Session = sessionmaker(bind=engine)   # Cria uma fábrica de sessões para o banco de dados

def criar_tabela():
    """Cria a tabela no banco de dados, se não existir."""
    Base.metadata.create_all(engine)  # Cria todas as tabelas definidas no modelo do banco
    print("Tabela criada/verificada com sucesso!")  # Exibe mensagem de sucesso

# Função para extrair os dados do preço do Bitcoin via API do Coinbase
def extract_dados_bitcoin():
    url = "https://api.coinbase.com/v2/prices/spot"  # Define a URL do endpoint para obter o preço spot do Bitcoin
    response = requests.get(url)  # Realiza uma requisição GET para a URL definida
    dados = response.json()       # Converte a resposta da requisição para um dicionário Python usando o método json()
    return dados

def transform_dados_bitcoin(dados_json):
    """Transforma os dados brutos da API e adiciona timestamp."""
    valor = float(dados_json['data']['amount'])      # Extrai e converte o valor do Bitcoin para float
    criptomoeda = dados_json['data']['base']         # Extrai o nome da criptomoeda
    moeda = dados_json['data']['currency']           # Extrai a moeda de referência
    timestamp = datetime.now()                       # Obtém o timestamp atual
    
    dados_tratados = {                              # Cria um dicionário com os dados tratados
        "valor": valor,
        "criptomoeda": criptomoeda,
        "moeda": moeda,
        "timestamp": timestamp
    }
    return dados_tratados                           # Retorna o dicionário tratado

def salvar_dados_postgres(dados):
    """Salva os dados no banco PostgreSQL."""
    session = Session()                             # Cria uma nova sessão de banco de dados
    novo_registro = BitcoinPreco(**dados)           # Cria um novo objeto BitcoinPreco com os dados tratados
    session.add(novo_registro)                      # Adiciona o novo registro à sessão
    session.commit()                                # Salva as alterações no banco de dados
    session.close()                                 # Fecha a sessão
    print(f"[{dados['timestamp']}] Dados salvos no PostgreSQL!")  # Exibe mensagem de sucesso

if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente
    criar_tabela()  # Cria/verifica a tabela no banco de dados
    print("Iniciando ETL com atualização a cada 15 segundos... (CTRL+C para interromper)")  # Mensagem inicial

    while True:  # Loop infinito para executar o ETL periodicamente
        try:
            dados_json = extract_dados_bitcoin()  # Extrai os dados da API
            if dados_json:  # Se os dados foram extraídos com sucesso
                dados_tratados = transform_dados_bitcoin(dados_json)  # Trata os dados extraídos
                print("Dados Tratados:", dados_tratados)           # Exibe os dados tratados no terminal
                salvar_dados_postgres(dados_tratados)              # Salva os dados tratados no banco de dados
            time.sleep(15)  # Aguarda 15 segundos antes da próxima execução
        except KeyboardInterrupt:  # Captura interrupção do usuário (CTRL+C)
            print("\nProcesso interrompido pelo usuário. Finalizando...")  # Mensagem de finalização
            break  # Sai do loop
        except Exception as e:  # Captura qualquer outro erro
            print(f"Erro durante a execução: {e}")  # Exibe mensagem de erro
            time.sleep(15)  # Aguarda 15 segundos antes de tentar novamente