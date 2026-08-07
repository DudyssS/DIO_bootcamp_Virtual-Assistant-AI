import streamlit as st
from config import PERGUNTAS_SUGERIDAS
from agente import carregar_base_conhecimento, buscar_resposta, obter_perguntas_relacionadas

st.set_page_config(page_title="RH.IA - Assistente Virtual de RH", page_icon="🤖")


def processar_pergunta(pergunta, base):
    st.session_state.historico.append(("user", pergunta))
    resposta, categoria, score = buscar_resposta(pergunta, base)
    st.session_state.historico.append(("assistant", resposta, categoria, score))
    st.session_state.categoria_atual = categoria
    st.session_state.ultima_pergunta = pergunta


def mudar_de_assunto():
    st.session_state.categoria_atual = None
    st.session_state.ultima_pergunta = None


st.title("🤖 RH.IA — Assistente Virtual de RH")
st.write("Tire suas dúvidas sobre férias, banco de horas, benefícios, licenças e políticas internas.")

base_conhecimento = carregar_base_conhecimento()

if "historico" not in st.session_state:
    st.session_state.historico = []
if "categoria_atual" not in st.session_state:
    st.session_state.categoria_atual = None
if "ultima_pergunta" not in st.session_state:
    st.session_state.ultima_pergunta = None

# Mostra o histórico da conversa
for item in st.session_state.historico:
    if item[0] == "user":
        with st.chat_message("user"):
            st.write(item[1])
    else:
        _, resposta, categoria, score = item
        with st.chat_message("assistant"):
            st.write(resposta)
            if categoria:
                st.caption(f"Categoria: {categoria} · confiança: {score:.0%}")

# Área de sugestões
if st.session_state.categoria_atual is None:
    # Ainda não há assunto definido: mostra uma pergunta de cada categoria
    st.write("**Experimente perguntar:**")
    colunas = st.columns(len(PERGUNTAS_SUGERIDAS))
    for coluna, pergunta_sugerida in zip(colunas, PERGUNTAS_SUGERIDAS):
        if coluna.button(pergunta_sugerida):
            processar_pergunta(pergunta_sugerida, base_conhecimento)
            st.rerun()
else:
    # Já há um assunto: mostra outras perguntas da mesma categoria
    relacionadas = obter_perguntas_relacionadas(
        base_conhecimento,
        st.session_state.categoria_atual,
        st.session_state.ultima_pergunta
    )
    if relacionadas:
        st.write(f"**Perguntas relacionadas sobre {st.session_state.categoria_atual}:**")
        for pergunta_relacionada in relacionadas:
            if st.button(pergunta_relacionada):
                processar_pergunta(pergunta_relacionada, base_conhecimento)
                st.rerun()

    if st.button("🔄 Mudar de assunto"):
        mudar_de_assunto()
        st.rerun()

# Campo de digitação livre (sempre disponível)
pergunta = st.chat_input("Digite sua pergunta sobre RH...")
if pergunta:
    processar_pergunta(pergunta, base_conhecimento)
    st.rerun()
