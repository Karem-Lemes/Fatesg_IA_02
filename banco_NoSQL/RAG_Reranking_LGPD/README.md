# RAG com Reranking — LGPD

**Trabalho Final N2 — Banco de Dados / Inteligência Artificial**  
**SENAI FATESG — 2025**

---

## O que é este projeto?

Um sistema de perguntas e respostas sobre a **Lei Geral de Proteção de Dados (LGPD — Lei nº 13.709/2018)**, construído com a arquitetura **RAG com Reranking**.

O sistema busca os trechos mais relevantes da lei e gera respostas precisas citando os artigos correspondentes — sem inventar informação.

---

## O que é RAG?

**RAG (Retrieval-Augmented Generation)** é uma arquitetura que combina busca em base de dados com geração de texto por LLM.

Em vez de depender só da memória do modelo, o sistema **busca os trechos relevantes primeiro** e os envia como contexto para o LLM responder. O resultado é mais preciso, rastreável e sem alucinações.

---

## Por que Reranking?

### Sem Reranking

```
Pergunta do usuário
        ↓
Embedding da pergunta (vetor)
        ↓
Qdrant busca os 5 mais similares por distância de cosseno
        ↓
LLM responde com esses 5 trechos
```

A busca vetorial mede **similaridade superficial** entre vetores.
Pode trazer trechos que parecem próximos em significado geral,
mas não são os mais relevantes para aquela pergunta específica.

---

### Com Reranking ⭐

```
Pergunta do usuário
        ↓
Embedding da pergunta (vetor)
        ↓
Qdrant busca os 20 mais similares por distância de cosseno
        ↓
  ★ RERANKER (Cross-encoder) ★
  Lê cada par (pergunta + trecho) junto
  e calcula um score de relevância real
  Reordena os 20 → seleciona os Top 5
        ↓
LLM responde com os 5 trechos mais relevantes
```

O **cross-encoder** é um modelo especializado em medir relevância.
Ele lê a pergunta e o trecho **juntos**, não separadamente.
É mais lento, mas muito mais preciso.

Por isso o pipeline usa os dois em sequência:
- Vetorial: filtra rápido (1000 → 20)
- Reranker: refina com precisão (20 → 5)

---

## Tecnologias utilizadas

| Componente | Tecnologia |
|---|---|
| Banco vetorial | Qdrant Cloud |
| Embeddings | `paraphrase-multilingual-mpnet-base-v2` |
| Reranker | `cross-encoder/ms-marco-MiniLM-L-6-v2` |
| LLM | Maritaca AI (sabia-3) |
| Interface | Gradio |
| Ambiente | Google Colab |

---

## Como rodar

### Pré-requisitos

- Conta no [Qdrant Cloud](https://cloud.qdrant.io) (gratuito)
- Chave de API da Maritaca AI
- Google Colab

### Passo a passo

1. Abra o notebook `RAG_Reranking_LGPD.ipynb` no Google Colab
2. Execute as células em ordem
3. Na célula de configuração, insira:
   - `QDRANT_URL` — URL do seu cluster Qdrant
   - `QDRANT_API_KEY` — chave do Qdrant Cloud
   - `MARITACA_API_KEY` — chave da Maritaca AI
4. Execute todas as células até a interface Gradio
5. Acesse o link público gerado pelo Gradio

---

## Exemplos de perguntas e respostas

**Pergunta:** Quais são os direitos do titular dos dados segundo a LGPD?

**Resposta:** Os direitos do titular estão previstos no Art. 18 e incluem: confirmação da existência de tratamento, acesso aos dados, correção de dados inexatos, anonimização ou eliminação de dados desnecessários, portabilidade, eliminação dos dados tratados com consentimento, informação sobre compartilhamento, e revogação do consentimento.

---

**Pergunta:** O que são dados pessoais sensíveis?

**Resposta:** Conforme o Art. 5º, II, dados pessoais sensíveis são aqueles sobre origem racial ou étnica, convicção religiosa, opinião política, filiação sindical, dados referentes à saúde ou vida sexual, dados genéticos ou biométricos quando vinculados a uma pessoa natural.

---

**Pergunta:** Quais são as penalidades para quem descumprir a LGPD?

**Resposta:** O Art. 52 prevê: advertência, multa simples de até 2% do faturamento limitada a R$ 50 milhões por infração, multa diária, publicização da infração, bloqueio e eliminação dos dados pessoais.

---

## Limitações

- O reranker foi treinado majoritariamente em inglês — pode perder precisão em casos limítrofes em português
- A base de dados cobre os principais artigos da LGPD, não a lei completa
- O Qdrant Cloud gratuito tem limite de armazenamento
- A sessão do Colab se encerra após inatividade, perdendo os dados indexados em memória

---

## Aprendizados

- A diferença entre **bi-encoder** (embedding) e **cross-encoder** (reranker) é fundamental para entender RAG avançado
- O banco vetorial não define a arquitetura RAG — a **estratégia de recuperação** é que define
- Reranking melhora significativamente a qualidade das respostas em perguntas ambíguas
- A sobreposição entre chunks evita perda de contexto nas fronteiras dos trechos
- Gradio permite criar interfaces funcionais e públicas diretamente no Colab sem infraestrutura adicional
