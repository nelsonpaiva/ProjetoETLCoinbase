# ProjetoETLCoinbase

## Descrição

Este projeto demonstra um fluxo ETL (Extract, Transform, Load) utilizando Python para consumir APIs públicas, incluindo a API do Coinbase para preços de criptomoedas e exemplos de integração com a API da OpenAI. O objetivo é apresentar técnicas de extração de dados, manipulação de JSON e boas práticas de autenticação.

## Estrutura do Projeto

```
.env                  # Variáveis de ambiente (ex: chaves de API)
.gitignore            # Arquivos e pastas ignorados pelo Git
main.py               # Arquivo principal do projeto
requirements.txt      # Dependências do projeto
exemplos/             # Exemplos de uso de APIs
    exemplo_01.py     # Requisições GET/POST básicas
    exemplo_02.py     # Consumo de API e manipulação de JSON
    exemplo_03.py     # Requisições GET com parâmetros e tratamento de resposta
    exemplo_04.py     # Requisições GET com parâmetros e cabeçalhos customizados
    exemplo_05.py     # Consulta ao preço do Bitcoin via API Coinbase
    exemplo_06.py     # Consulta à API OpenAI (chave fixa)
    exemplo_06.01.py  # Consulta à API OpenAI usando variável de ambiente
    exemplo_07.py     # Função para consultar OpenAI com tratamento de erros
```

## Instalação

Instale as dependências do projeto:

```sh
pip install -r requirements.txt
```

## Configuração

Crie um arquivo `.env` com sua chave da OpenAI:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## Exemplos de Uso

### 1. Requisições HTTP Básicas

Veja [exemplos/exemplo_01.py](exemplos/exemplo_01.py) para requisições GET e POST simples usando a biblioteca `requests`.

### 2. Consumo de APIs e Manipulação de JSON

- [exemplos/exemplo_02.py](exemplos/exemplo_02.py): Consome uma API REST e imprime o resultado em JSON.
- [exemplos/exemplo_03.py](exemplos/exemplo_03.py) e [exemplos/exemplo_04.py](exemplos/exemplo_04.py): Realizam requisições GET com parâmetros e exibem informações sobre o status da resposta.

### 3. Consulta ao Preço do Bitcoin

- [exemplos/exemplo_05.py](exemplos/exemplo_05.py): Consulta o preço do Bitcoin em USD via API do Coinbase.

### 4. Integração com a API da OpenAI

- [exemplos/exemplo_06.py](exemplos/exemplo_06.py): Consulta à API da OpenAI usando chave fixa.
- [exemplos/exemplo_06.01.py](exemplos/exemplo_06.01.py): Consulta à API da OpenAI usando chave via variável de ambiente.
- [exemplos/exemplo_07.py](exemplos/exemplo_07.py): Função robusta para consultar a OpenAI, com tratamento de erros e retorno do texto gerado.

## Segurança

- Nunca compartilhe sua chave de API publicamente.
- Use o arquivo `.env` para armazenar credenciais sensíveis.
- O arquivo `.gitignore` já está configurado para ignorar `.env` e ambientes virtuais.

## Dependências

Veja [requirements.txt](requirements.txt) para a lista completa de bibliotecas utilizadas.

## Execução dos Exemplos

Execute qualquer exemplo diretamente pelo terminal:

```sh
python exemplos/exemplo_05.py
```

## Licença

Este projeto é apenas para fins educacionais.