import os
import requests
import json

# Lê a chave da API de uma variável de ambiente (boa prática de segurança)
API_KEY = os.getenv("OPENAI_API_KEY")
URL = "https://api.openai.com/v1/chat/completions"

def consultar_openai(prompt: str, modelo: str = "gpt-3.5-turbo",
                     max_tokens: int = 100, temperatura: float = 0.7) -> str:
    """
    Consulta a API da OpenAI enviando um prompt e retorna apenas o texto da resposta.

    :param prompt: Texto enviado para o modelo (pergunta ou instrução).
    :param modelo: Modelo da OpenAI a ser usado (padrão: gpt-3.5-turbo).
    :param max_tokens: Número máximo de tokens na resposta.
    :param temperatura: Controla criatividade (0 = resposta determinística).
    :return: Texto da resposta gerada pela API.
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer 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"
    }

    data = {
        "model": modelo,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": temperatura
    }

    try:
        response = requests.post(URL, headers=headers, data=json.dumps(data), timeout=15)
        response.raise_for_status()
        resposta_json = response.json()

        if "choices" in resposta_json and len(resposta_json["choices"]) > 0:
            return resposta_json["choices"][0]["message"]["content"].strip()
        else:
            return "❌ A resposta não contém choices válidos."

    except requests.exceptions.RequestException as e:
        return f"❌ Erro de requisição HTTP: {e}"
    except (KeyError, ValueError) as e:
        return f"❌ Erro ao processar resposta JSON: {e}"


# Exemplo de uso:
if __name__ == "__main__":
    print(consultar_openai("Qual é a capital da França?"))
