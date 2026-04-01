import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Função para ler seus arquivos SQL
def ler_sql(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        return f.read()

# 2. Configuração da Página
st.set_page_config(page_title="Dashboard Walmart", layout="wide")
st.title("📊 Painel de Controle - Big Data do Walmart")
st.markdown("---")

# 3. Conexão com o Banco
engine = create_engine('postgresql://postgres:Kk*991004@localhost:5433/db_projeto_walmart')

# --- PRIMEIRA LINHA: SAZONALIDADE E FERIADOS ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Tendência de Vendas (Sazonalidade)")
    query_saz = ler_sql('Select_sazonalidade.sql')
    df_saz = pd.read_sql(query_saz, engine)
    fig1, ax1 = plt.subplots(figsize=(8, 5))
    sns.lineplot(data=df_saz, x=df_saz.columns[0], y=df_saz.columns[1], marker='o', ax=ax1)
    st.pyplot(fig1)

with col2:
    st.subheader("🏖️ Impacto dos Feriados")
    query_fer = ler_sql('Select_impacto_feriados.sql')
    df_fer = pd.read_sql(query_fer, engine)
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    sns.barplot(data=df_fer, x=df_fer.columns[0], y=df_fer.columns[1], palette='Set2', ax=ax2)
    st.pyplot(fig2)

st.markdown("---")

# --- SEGUNDA LINHA: CURVA ABC E LOJAS ---
col3, col4 = st.columns(2)

with col3:
    st.subheader("🏆 Top 10 Departamentos (Curva ABC)")
    query_abc = ler_sql('Select_curvaABC_depto.sql')
    df_abc = pd.read_sql(query_abc, engine)
    fig3, ax3 = plt.subplots(figsize=(8, 5))
    sns.barplot(data=df_abc.head(10), x=df_abc.columns[0], y=df_abc.columns[1], palette='viridis', ax=ax3)
    plt.xticks(rotation=45)
    st.pyplot(fig3)

with col4:
    st.subheader("⚠️ Lojas com Menor Desempenho")
    query_lojas = ler_sql('Select_lojas_ineficientes.sql')
    df_lojas = pd.read_sql(query_lojas, engine)
    
    # 1. Garantir que o ID da Loja seja texto (para o gráfico não tentar somar os números)
    df_lojas[df_lojas.columns[0]] = df_lojas[df_lojas.columns[0]].astype(str)
    
    # 2. Garantir que a coluna de vendas seja numérica (float)
    # Vamos pegar a última coluna, que geralmente é onde fica o faturamento no SQL
    df_lojas[df_lojas.columns[-1]] = pd.to_numeric(df_lojas[df_lojas.columns[-1]])

    fig4, ax4 = plt.subplots(figsize=(8, 5))
    
    # Criando o gráfico forçando X e Y
    sns.barplot(
        data=df_lojas.head(10), # Pega as 10 primeiras (as piores se o SQL estiver ASC)
        x=df_lojas.columns[0],  # ID da Loja
        y=df_lojas.columns[-1], # Faturamento Total (Última coluna)
        palette='Reds_r', 
        ax=ax4
    )
    
    plt.xticks(rotation=45)
    plt.ylabel("Faturamento Total ($)")
    plt.xlabel("ID da Loja")
    st.pyplot(fig4)

    # streamlit run dashboard_walmart.py