# RAG Avançado — Resolução CNJ nº 615/2025

## Descrição
Implementação de um sistema de Recuperação Aumentada por Geração (RAG) Avançado,
utilizando como corpus a Resolução CNJ nº 615/2025, que estabelece diretrizes para
o desenvolvimento, utilização e governança de soluções de Inteligência Artificial
no Poder Judiciário brasileiro.

## Técnicas Implementadas

### Pré-recuperação
- Chunking com sobreposição (sliding window) para evitar perda de contexto nas bordas
- Enriquecimento com metadados por artigo e capítulo para rastreabilidade

### Recuperação
- Banco vetorial ChromaDB com busca por similaridade
- Embeddings multilíngues: `paraphrase-multilingual-MiniLM-L12-v2`
- Recuperação Top-K inicial

### Pós-recuperação — Re-ranqueamento
- Recálculo de similaridade por cosseno entre a pergunta e cada chunk recuperado
- Seleção dos Top-N mais relevantes antes do envio à LLM
- Reduz contexto desnecessário e melhora a precisão da resposta

### Geração
- LLM: Maritaca AI `sabia-3`
- Prompt estruturado com contexto restrito aos chunks reranqueados

## Tecnologias
- Python 3
- ChromaDB
- Sentence Transformers
- Maritaca AI (sabia-3)
- Google Colab

## Corpus
Resolução CNJ nº 615, de 11 de março de 2025  
Fonte: https://atos.cnj.jus.br/files/original1555302025031467d4517244566.pdf

## Como executar
1. Abrir o notebook no Google Colab
2. Adicionar a chave `MARITACA_API_KEY` nos Secrets do Colab
3. Executar os blocos em ordem

## Disciplina
Inteligência Artificial — SENAI FATESG  
Semestre: 2º semestre / 2025
