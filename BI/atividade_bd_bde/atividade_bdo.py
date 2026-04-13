import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

arquivos = [
    ("goiania_docentes.html",              "Goiânia",              "Docentes_Total"),
    ("goiania_alunos.html",                "Goiânia",              "Matriculas_Fundamental_Total"),
    ("rio_verde_docentes.html",            "Rio Verde",            "Docentes_Total"),
    ("rio_verde_alunos.html",              "Rio Verde",            "Matriculas_Fundamental_Total"),
    ("aparecida_de_goiania_docentes.html", "Aparecida de Goiânia", "Docentes_Total"),
    ("aparecida_de_goiania_alunos.html",   "Aparecida de Goiânia", "Matriculas_Fundamental_Total"),
]

def ler_html(arquivo, municipio, variavel):
    with open(arquivo, "r", encoding="windows-1252", errors="ignore") as f:
        soup = BeautifulSoup(f, "html.parser")

    tabela = soup.find("table")
    if not tabela:
        print(f"TABELA NÃO ENCONTRADA: {arquivo}")
        return []

    linhas = tabela.find_all("tr")
    
    # Anos estão no cabeçalho dentro de <b>
    anos = []
    for td in linhas[1].find_all("td"):
        txt = td.get_text(strip=True)
        if txt.isdigit() and len(txt) == 4:
            anos.append(int(txt))
    
    print(f"  Anos encontrados: {anos}")

    registros = []
    for linha in linhas[2:]:
        colunas = linha.find_all("td")
        if len(colunas) <= 5:
            continue
        valores = colunas[5:]
        for i, ano in enumerate(anos):
            if i < len(valores):
                try:
                    val_txt = valores[i].get_text(strip=True).replace("\xa0", "").replace(".", "").replace(",", ".")
                    valor = float(val_txt) if val_txt else None
                except:
                    valor = None
                registros.append({
                    "municipio": municipio,
                    "variavel": variavel,
                    "ano": ano,
                    "valor": valor
                })
    return registros

# ============================================================
# CONSTRUIR DATAFRAME
# ============================================================
registros = []
for arq, mun, var in arquivos:
    dados = ler_html(arq, mun, var)
    print(f"{mun} | {var} | {len(dados)} registros")
    registros.extend(dados)

df_long = pd.DataFrame(registros)
df_long = df_long[df_long["ano"] >= 2014].copy()

print("\nTotal de registros:", len(df_long))
print(df_long.head(10))

# ============================================================
# EDA
# ============================================================
print("\n=== ESTRUTURA ===")
print(df_long.info())
print("\n=== DADOS FALTANTES ===")
print(df_long.isnull().sum())
print("\n=== ESTATÍSTICAS DESCRITIVAS ===")
print(df_long.groupby(["municipio", "variavel"], observed=True)["valor"].describe())

# Tratar faltantes
df_long["valor"] = pd.to_numeric(df_long["valor"], errors="coerce")
df_long["valor"] = (
    df_long
    .groupby(["municipio", "variavel"], observed=True)["valor"]
    .transform(lambda x: x.interpolate(method="linear").ffill().bfill())
)

# ============================================================
# KPIs
# ============================================================
df_pivot = df_long.pivot_table(
    index=["municipio", "ano"],
    columns="variavel",
    values="valor"
).reset_index()
df_pivot.columns.name = None

df_pivot["KPI1_Razao_Aluno_Docente"] = (
    df_pivot["Matriculas_Fundamental_Total"] / df_pivot["Docentes_Total"]
).round(2)

df_pivot = df_pivot.sort_values(["municipio", "ano"])

df_pivot["KPI2_Crescimento_Docentes_Pct"] = (
    df_pivot.groupby("municipio", observed=True)["Docentes_Total"]
    .pct_change() * 100
).round(2)

df_pivot["var_mat"] = df_pivot.groupby("municipio", observed=True)["Matriculas_Fundamental_Total"].pct_change()
df_pivot["var_doc"] = df_pivot.groupby("municipio", observed=True)["Docentes_Total"].pct_change()
df_pivot["KPI3_Pressao_Escolar"] = (df_pivot["var_mat"] - df_pivot["var_doc"]).round(4)

print("\n=== KPIs ===")
print(df_pivot[["municipio", "ano", "KPI1_Razao_Aluno_Docente",
                "KPI2_Crescimento_Docentes_Pct", "KPI3_Pressao_Escolar"]].to_string(index=False))

# ============================================================
# GRÁFICOS
# ============================================================
cidades = df_pivot["municipio"].unique()
fig, axes = plt.subplots(1, len(cidades), figsize=(6 * len(cidades), 5))
fig.suptitle("BI — Educação Básica em Goiás (2014–2024)", fontsize=14)

for ax, cidade in zip(axes, cidades):
    grupo = df_pivot[df_pivot["municipio"] == cidade]
    ax.plot(grupo["ano"], grupo["KPI1_Razao_Aluno_Docente"], marker="o", color="royalblue")
    ax.set_title(f"Alunos/Docente\n{cidade}")
    ax.set_xlabel("Ano")
    ax.set_ylabel("Razão")
    ax.grid(True)

for ax in axes:
    ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
    ax.set_xticks([2020, 2021, 2022, 2023, 2024])
    ax.set_xticklabels(['2020', '2021', '2022', '2023', '2024'])

plt.tight_layout()
plt.savefig("kpi_educacao_goias.png", dpi=150)
plt.show()