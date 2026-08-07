# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação foi feita de duas formas complementares:
1. **Testes estruturados:** perguntas com resposta esperada definida com base nos JSONs;
2. **Feedback real:** colegas testaram o agente e avaliaram as respostas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar sobre férias e receber a regra correta |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora da base e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido com a pergunta feita? | Pergunta sobre home office retorna a política de home office, não outra categoria |

> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5.

---

## Exemplos de Cenários de Teste

### Teste 1: Consulta direta na base
- **Pergunta:** "Quantos dias de férias eu tenho?"
- **Resposta esperada:** "30 dias corridos após completar 12 meses de trabalho"
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 2: Consulta com palavras diferentes da base
- **Pergunta:** "Dá pra receber em dinheiro parte das minhas férias?"
- **Resposta esperada:** Resposta sobre venda de férias / abono pecuniário
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo de RH
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que só trata de assuntos de RH
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 4: Informação inexistente na base
- **Pergunta:** "A empresa fornece notebook para home office?"
- **Resposta esperada:** Agente admite não ter essa informação e orienta a procurar o RH/TI
- **Resultado:** [x] Correto  [ ] Incorreto

---

## Resultados

**O que funcionou bem:**
- O agente respondeu corretamente perguntas com palavras próximas às da base de conhecimento (ex: "vender férias" e "receber em dinheiro parte das férias")
- O agente não inventou respostas quando a informação não estava na base, seguindo a regra de segurança do system prompt
- As respostas ficaram objetivas e no tom definido na persona

**O que pode melhorar:**
- Perguntas com sinônimos muito diferentes das perguntas cadastradas na base (ex: gírias) nem sempre foram reconhecidas corretamente
- A base de conhecimento pode ser expandida com mais variações de pergunta por categoria

---

## Métricas Avançadas (Opcional)

Métricas técnicas de observabilidade que podem ser incorporadas futuramente:
- Latência e tempo de resposta;
- Taxa de perguntas sem correspondência na base;
- Logs de perguntas frequentes para identificar lacunas na base de conhecimento.

Ferramentas como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/) podem ajudar nesse monitoramento em versões futuras do projeto.
