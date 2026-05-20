# Análise Exploratória de Dados — Superstore Sales Dataset

**Disciplina:** Big Data e Data Science
**Instituição:** FATESG
**Dupla:** Karem Lemes e Melissa Cunha 
---

## Descrição do Projeto

Este projeto consiste em uma análise exploratória completa (EDA) aplicada
à base de dados pública *Superstore Sales Dataset*, disponível no Kaggle.
O objetivo é extrair insights relevantes sobre o desempenho comercial de
uma rede varejista americana, aplicando técnicas de estatística descritiva,
visualização de dados e modelagem preditiva com Machine Learning.

---

## Base de Dados

| Atributo | Descrição |
|---|---|
| **Nome** | Superstore Sales Dataset |
| **Fonte** | [Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) |
| **Registros** | 9.994 linhas |
| **Variáveis** | 21 colunas |
| **Período** | 2014 a 2017 |

### Principais variáveis analisadas

| Variável | Tipo | Descrição |
|---|---|---|
| Order Date | Data | Data do pedido |
| Ship Mode | Categórica | Modalidade de envio |
| Segment | Categórica | Segmento do cliente |
| Region | Categórica | Região geográfica |
| Category | Categórica | Categoria do produto |
| Sales | Numérica | Valor da venda (USD) |
| Quantity | Numérica | Quantidade vendida |
| Discount | Numérica | Desconto aplicado (0 a 1) |
| Profit | Numérica | Lucro do pedido (USD) |

---

## Tecnologias Utilizadas

- Python 3
- Google Colab
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## Estrutura do Repositório
├── Projeto Analise de Dados_SuperStore.ipynb  # Notebook principal
├── Sample - Superstore.csv                    # Base de dados
└── README.md                                  # Este arquivo

---

## Etapas da Análise

### 1. Tratamento e Qualidade dos Dados
- Verificação de valores nulos — nenhum encontrado
- Verificação de duplicatas — nenhuma encontrada
- Conversão de variáveis de data
- Detecção de outliers via boxplot

### 2. Estatísticas Descritivas
Calculadas para as variáveis numéricas: média, mediana, moda,
desvio padrão, variância, mínimo, máximo e quartis (Q1, Q2, Q3).

### 3. Visualizações

| Gráfico | Descrição |
|---|---|
| Boxplot | Detecção de outliers em Vendas, Lucro e Desconto |
| Barras | Total de vendas por categoria |
| Barras | Total de lucro por categoria |
| Linha | Evolução anual de vendas (2014–2017) |
| Barras | Total de vendas por região |
| Dispersão | Relação entre desconto e lucro |
| Heatmap | Mapa de correlação entre variáveis numéricas |

### 4. Modelagem Preditiva (Machine Learning)

**Problema:** Classificação binária — prever se um pedido resultará
em lucro ou prejuízo.

**Justificativa:** A variável alvo *Lucrativo* (1 = lucro, 0 = prejuízo)
foi derivada da variável *Profit*, tornando o problema adequado para
algoritmos de classificação.

**Algoritmos aplicados:**

| Modelo | Acurácia | Precision | Recall | F1-Score |
|---|---|---|---|---|
| Árvore de Decisão | 94.3% | 0.95 | 0.94 | 0.94 |
| Random Forest Classifier | 92.9% | 0.93 | 0.93 | 0.93 |

---

## Principais Conclusões

- **Technology** liderou em vendas ($836.154), mas as três categorias
apresentam desempenho equilibrado
- As regiões **West e East** concentram mais de 60% das vendas totais,
enquanto **South** representa oportunidade de expansão
- Descontos acima de **40%** resultam majoritariamente em prejuízo —
a política de descontos atual compromete a margem do negócio
- As vendas cresceram **20%** de 2016 para 2017, indicando expansão sólida
- A **Árvore de Decisão** superou o Random Forest com 94.3% de acurácia,
demonstrando que existem regras de decisão claras e interpretáveis que
separam pedidos lucrativos de não lucrativos

---

## Como Executar

1. Acesse o [Google Colab](https://colab.research.google.com)
2. Faça upload do arquivo `Projeto Analise de Dados_SuperStore.ipynb`
3. Execute as células em ordem
4. Quando solicitado, faça upload do arquivo `Sample - Superstore.csv`
