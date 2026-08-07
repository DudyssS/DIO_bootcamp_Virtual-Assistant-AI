# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `ferias.json` | JSON | Responder dúvidas sobre férias, venda de dias e fracionamento |
| `banco_de_horas.json` | JSON | Responder dúvidas sobre acúmulo, compensação e prazo do banco de horas |
| `beneficios.json` | JSON | Responder dúvidas sobre plano de saúde, vale-refeição, vale-transporte etc. |
| `licencas.json` | JSON | Responder dúvidas sobre licença médica, maternidade e paternidade |
| `politicas_gerais.json` | JSON | Responder dúvidas sobre home office, código de conduta e canal de ética |

---

## Adaptações nos Dados

> Os dados originais do repositório base (focados em contexto financeiro: transações, perfil de investidor, produtos financeiros) foram substituídos por uma base de conhecimento nova, voltada para Recursos Humanos. Cada categoria foi organizada em um arquivo JSON separado, no formato "pergunta/resposta", com 5 perguntas frequentes por categoria — incluindo, propositalmente, ao menos um exemplo de pergunta fora do escopo, para documentar como o agente se comporta quando não tem a resposta.

---

## Estratégia de Integração

### Como os dados são carregados?
> Os 5 arquivos JSON são carregados no início da execução do app (`src/app.py`), sendo unificados em uma única lista de perguntas e respostas com suas respectivas categorias.

### Como os dados são usados no prompt?
> A pergunta do colaborador é comparada com as perguntas da base de conhecimento (busca por similaridade de texto/palavras-chave). Se houver uma correspondência suficientemente próxima, a resposta correspondente é retornada. Se não houver correspondência, o agente retorna a resposta padrão de limitação ("não tenho essa informação..."), sem tentar gerar uma resposta nova.

---

## Exemplo de Contexto Montado

```
Pergunta do colaborador: "Posso vender minhas férias?"

Busca na base de conhecimento:
- Categoria: ferias
- Pergunta mais próxima: "Posso vender parte das minhas férias?"
- Similaridade: alta

Resposta retornada:
"Sim. É possível vender até 10 dias de férias (1/3 do período), 
conhecido como 'abono pecuniário'. A solicitação deve ser feita 
ao RH com pelo menos 30 dias de antecedência."
```

```
Pergunta do colaborador: "Qual o valor do meu salário?"

Busca na base de conhecimento:
- Nenhuma categoria/pergunta correspondente encontrada

Resposta retornada:
"Não tenho essa informação na minha base de conhecimento no 
momento. Recomendo falar diretamente com o time de RH."
```
