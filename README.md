# HR Assistant AI

Este projeto foi desenvolvido como parte do bootcamp da **Digital Innovation One (DIO)**, no desafio **"Construa Seu Assistente Virtual Com Inteligência Artificial"**, com o objetivo de criar um assistente capaz de responder dúvidas frequentes do setor de **Recursos Humanos**.

O **HR Assistant AI** utiliza uma base de conhecimento estruturada para fornecer respostas claras e objetivas sobre férias, banco de horas, benefícios, licenças e políticas internas. O assistente responde apenas com base nas informações disponíveis em sua base de conhecimento, evitando respostas inventadas e informando o usuário quando não houver dados suficientes.

---

## Contexto

Em empresas de todos os portes, grande parte das solicitações enviadas ao setor de Recursos Humanos corresponde a dúvidas recorrentes — como funciona o banco de horas, quantos dias de férias posso vender, como solicitar licença médica, como consultar meus benefícios. Responder continuamente essas perguntas consome tempo da equipe de RH e atrasa atividades mais estratégicas.

O **HR Assistant AI** propõe usar Inteligência Artificial para:

- **Automatizar o atendimento** de dúvidas recorrentes de RH
- **Padronizar** as respostas para toda a empresa
- **Garantir segurança e confiabilidade** nas respostas (anti-alucinação)
- **Liberar tempo** da equipe de RH para atividades estratégicas

---

## Objetivo

Desenvolver um assistente virtual capaz de:

- compreender perguntas realizadas pelos colaboradores;
- consultar uma base de conhecimento previamente estruturada;
- responder utilizando apenas informações disponíveis;
- evitar respostas inventadas (*hallucinations*);
- orientar o usuário quando não houver informação suficiente.

---

## Solução

O **HR Assistant AI** atua como um assistente virtual especializado em Recursos Humanos. Sempre que recebe uma pergunta, ele:

1. interpreta a solicitação do usuário;
2. consulta sua Base de Conhecimento;
3. identifica a resposta adequada;
4. apresenta uma resposta objetiva;
5. informa quando não possui conhecimento suficiente.

Dessa forma, o colaborador recebe respostas rápidas e padronizadas, enquanto o setor de RH reduz o volume de atendimentos repetitivos.

**Funcionalidades:**

- Atendimento automatizado de dúvidas de RH
- Consulta à Base de Conhecimento
- Respostas objetivas e padronizadas
- Bloqueio de respostas fora da base de conhecimento
- Interface simples para conversação
- Respostas organizadas por categoria

**Público-alvo:** colaboradores, equipes de Recursos Humanos, gestores, empresas e estudantes interessados em IA aplicada ao ambiente corporativo.

---

## O Que Você Deve Entregar

### 1. Documentação do Agente

Define **o que** o agente faz e **como** ele funciona:

- **Caso de Uso:** dúvidas frequentes de RH (férias, banco de horas, benefícios, licenças, políticas gerais)
- **Persona e Tom de Voz:** como o agente se comporta e se comunica
- **Arquitetura:** fluxo de dados e integração com a base de conhecimento
- **Segurança:** como evitar alucinações e garantir respostas confiáveis

📄 **Template:** [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md)

---

### 2. Base de Conhecimento

Dados mockados disponíveis na pasta [`data/`](./data/):

| Arquivo                   | Formato | Descrição                                    |
| -------------------------- | ------- | --------------------------------------------- |
| `ferias.json`               | JSON    | Perguntas e respostas sobre férias             |
| `banco_de_horas.json`       | JSON    | Perguntas e respostas sobre banco de horas     |
| `beneficios.json`           | JSON    | Perguntas e respostas sobre benefícios         |
| `licencas.json`             | JSON    | Perguntas e respostas sobre licenças           |
| `politicas_gerais.json`     | JSON    | Código de conduta, home office e outras políticas |

📄 **Template:** [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md)

---

### 3. Prompts do Agente

Documenta os prompts que definem o comportamento do agente:

- **System Prompt:** instruções gerais de comportamento e restrições
- **Exemplos de Interação:** cenários de uso com entrada e saída esperada
- **Tratamento de Edge Cases:** como o agente lida com situações-limite

📄 **Template:** [`docs/03-prompts.md`](./docs/03-prompts.md)

---

### 4. Aplicação Funcional

Protótipo funcional do assistente:

- Chatbot interativo (Streamlit)
- Busca na base de conhecimento
- Interface simples de conversação

📁 **Pasta:** [`src/`](./src/)

---

### 5. Avaliação e Métricas

Como a qualidade do agente foi avaliada:

**Métricas Sugeridas:**

- Precisão/assertividade das respostas
- Taxa de respostas seguras (sem alucinações)
- Coerência com a pergunta do colaborador

📄 **Template:** [`docs/04-metricas.md`](./docs/04-metricas.md)

---

### 6. Pitch

Pitch de 3 minutos (estilo elevador) apresentando:

- Qual problema o agente resolve?
- Como ele funciona na prática?
- Por que essa solução é útil para a empresa?

📄 **Template:** [`docs/05-pitch.md`](./docs/05-pitch.md)

---

## Ferramentas Utilizadas

| Categoria           | Ferramentas                                                        |
| ------------------- | ------------------------------------------------------------------- |
| **Desenvolvimento** | [Streamlit](https://streamlit.io/), [Google Colab](https://colab.research.google.com/) |
| **LLM (opcional)**  | [Gemini](https://gemini.google.com/), [Ollama](https://ollama.ai/) |
| **Diagramas**       | [Mermaid](https://mermaid.js.org/)|

---

## Estrutura do Repositório

```
📁 hr-assistant-ai/
│
├── 📄 README.md
│
├── 📁 data/                          # Dados mockados para o agente
│   ├── ferias.json
│   ├── banco_de_horas.json
│   ├── beneficios.json
│   ├── licencas.json
│   └── politicas_gerais.json
│
├── 📁 docs/                          # Documentação do projeto
│   ├── 01-documentacao-agente.md     # Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md       # Estratégia de dados
│   ├── 03-prompts.md                 # Engenharia de prompts
│   ├── 04-metricas.md                # Avaliação e métricas
│   └── 05-pitch.md                   # Roteiro do pitch
│
├── 📁 src/                           # Código da aplicação
│   └── app.py
│
└── 📁 assets/                        # Imagens e diagramas
    └── ...
```

---

## Dicas Finais

1. **Comece pelo prompt:** um bom system prompt é a base de um agente eficaz
2. **Use os dados mockados:** eles garantem consistência e evitam problemas com dados sensíveis
3. **Foque na segurança:** em RH, dados incorretos sobre benefícios ou licenças podem gerar problemas reais — evitar alucinações é crítico
4. **Teste cenários reais:** simule perguntas que um colaborador faria de verdade
5. **Seja direto no pitch:** 3 minutos passam rápido, vá ao ponto
