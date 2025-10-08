from sqlalchemy.orm import declarative_base #faz a conversão de objetos python para tabelas relacionais
from sqlalchemy import Column, Float, String, Integer, DateTime #atributos que vou usar para criar minha tabela
from datetime import datetime #ter o datetime para pegar o timestamp

Base = declarative_base() #cria a base do meu banco de dados

class BitcoinPreco(Base): #cria a classe que vai representar minha tabela no banco de dados
    __tablename__ = "bitcoin_preco" #nome da tabela no banco de dados

    id = Column(Integer, primary_key=True, autoincrement=True) #cria a coluna id que é a chave primária e é auto incrementada
    valor = Column(Float, nullable=False) #cria a coluna valor que é do tipo float e não pode ser nula
    criptomoeda = Column(String(50), nullable=False) #cria a coluna criptomoeda que é do tipo string e não pode ser nula
    moeda = Column(String(10), nullable=False) #cria a coluna moeda que é do tipo string e não pode ser nula
    timestamp = Column(DateTime, default=datetime.now) #cria a coluna timestamp que é do tipo datetime e não pode ser nula. O valor padrão é a data e hora atual em UTC

    #def __repr__(self): #método especial que retorna uma representação em string do objeto
        #return f"<BitcoinPreco(id={self.id}, valor={self.valor}, criptomoeda='{self.criptomoeda}', moeda='{self.moeda}', timestamp='{self.timestamp}')>" #retorna uma string formatada com os atributos do objeto

