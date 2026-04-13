# Atividade BI — Análise da Educação Básica em Goiás

## 📚 Descrição
Análise exploratória de dados (EDA) e cálculo de KPIs para Business Intelligence,
utilizando dados do Painel Municipal do IMB-GO (Instituto Mauro Borges de Estatísticas
e Estudos Socioeconômicos do Estado de Goiás).

## 🗂️ Variáveis Analisadas
| Código | Variável | Fonte |
|--------|----------|-------|
| 218 | Docentes - Total | MEC/INEP e SEE |
| 164 | Matrículas no Ensino Fundamental - Total | MEC/INEP e SEE |

## 🏙️ Municípios
- Goiânia
- Rio Verde
- Aparecida de Goiânia

## 📅 Período
2020 a 2024

## 📁 Arquivos
| Arquivo | Descrição |
|---------|-----------|
| `atividade_bdo.py` | Script principal com EDA e KPIs |
| `goiania_docentes.html` | Dados de docentes de Goiânia |
| `goiania_alunos.html` | Dados de matrículas de Goiânia |
| `rio_verde_docentes.html` | Dados de docentes de Rio Verde |
| `rio_verde_alunos.html` | Dados de matrículas de Rio Verde |
| `aparecida_de_goiania_docentes.html` | Dados de docentes de Aparecida de Goiânia |
| `aparecida_de_goiania_alunos.html` | Dados de matrículas de Aparecida de Goiânia |
| `kpi_educacao_goias.png` | Gráfico dos KPIs gerado |

## 🔍 EDA — Análise Exploratória
- Verificação da estrutura do dataset (tipos, shape)
- Identificação e tratamento de dados faltantes via interpolação linear
- Estatísticas descritivas por município e variável

## 📊 KPIs Calculados

### KPI 1 — Razão Aluno/Docente
**Fórmula:** `Matrículas Ensino Fundamental ÷ Total de Docentes`

Mede a carga média de alunos por docente. Valores acima de 25 indicam sobrecarga.
Todas as cidades apresentaram melhora no período, com Goiânia tendo a menor
razão (~12 alunos/docente) e Aparecida de Goiânia a maior (~16).

### KPI 2 — Taxa de Crescimento Anual de Docentes (%)
**Fórmula:** `((Docentes_ano / Docentes_ano-1) - 1) × 100`

Indica se o município está expandindo seu corpo docente ano a ano.
Valores positivos = contratação de novos professores.

### KPI 3 — Índice de Pressão Escolar
**Fórmula:** `% Variação Matrículas - % Variação Docentes`

Positivo = demanda de alunos crescendo mais que a oferta de docentes (pressão alta).
Negativo = docentes crescendo mais que matrículas (situação favorável).

## 📈 Resultados
As três cidades apresentaram tendência de **queda na razão aluno/docente** ao longo
do período, indicando melhora na adequação da formação docente. Aparecida de Goiânia
ainda concentra a maior pressão sobre os professores, enquanto Goiânia apresenta a melhor proporção.

## 🛠️ Tecnologias
- Python 3.13
- pandas, numpy, matplotlib, beautifulsoup4, requests

## 🔗 Fonte dos Dados
[Painel Municipal IMB-GO](https://painelmunicipal.imb.go.gov.br)