import json
import os
from difflib import SequenceMatcher
from config import DATA_DIR, LIMIAR_SIMILARIDADE


def carregar_base_conhecimento():
    """Lê todos os arquivos JSON da pasta data/ e monta a base de conhecimento."""
    base = []
    for arquivo in os.listdir(DATA_DIR):
        if arquivo.endswith(".json"):
            caminho = os.path.join(DATA_DIR, arquivo)
            with open(caminho, "r", encoding="utf-8") as f:
                conteudo = json.load(f)
                categoria = conteudo.get("categoria", arquivo)
                for item in conteudo.get("perguntas_frequentes", []):
                    base.append({
                        "categoria": categoria,
                        "pergunta": item["pergunta"],
                        "resposta": item["resposta"]
                    })
    return base


def calcular_similaridade(texto1, texto2):
    """Calcula o quão parecidas duas frases são (0 a 1)."""
    return SequenceMatcher(None, texto1.lower(), texto2.lower()).ratio()


def buscar_resposta(pergunta_usuario, base):
    """Procura na base de conhecimento a pergunta mais parecida com a do usuário."""
    melhor_item = None
    melhor_score = 0

    for item in base:
        score = calcular_similaridade(pergunta_usuario, item["pergunta"])
        if score > melhor_score:
            melhor_score = score
            melhor_item = item

    if melhor_item and melhor_score >= LIMIAR_SIMILARIDADE:
        return melhor_item["resposta"], melhor_item["categoria"], melhor_score
    else:
        return (
            "Não tenho essa informação na minha base de conhecimento no momento. "
            "Recomendo falar diretamente com o time de RH.",
            None,
            melhor_score
        )


def obter_perguntas_relacionadas(base, categoria, pergunta_atual, limite=3):
    """Retorna outras perguntas da mesma categoria, exceto a que já foi feita."""
    relacionadas = [
        item["pergunta"] for item in base
        if item["categoria"] == categoria and item["pergunta"] != pergunta_atual
    ]
    return relacionadas[:limite]
