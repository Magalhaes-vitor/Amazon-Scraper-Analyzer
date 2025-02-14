import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

# Título da aplicação
st.title("Amazon Fone Scraper & Analyzer")
st.write("Visualização e análise dos dados de fones de ouvido coletados da Amazon.")

# Função para carregar os dados do banco de dados
def carregar_dados():
    conn = sqlite3.connect('amazon_fones.db')
    query = "SELECT * FROM fones"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Carregar os dados
df = carregar_dados()

# Exibir os dados brutos
st.subheader("Dados Coletados")
st.write(df)

# Filtros interativos
st.sidebar.header("Filtros")
tipo_selecionado = st.sidebar.selectbox("Selecione o tipo de fone", ["Todos"] + list(df['tipo'].unique()))
conector_selecionado = st.sidebar.selectbox("Selecione o conector", ["Todos"] + list(df['conector'].unique()))
patrocinado_selecionado = st.sidebar.selectbox("Produtos patrocinados", ["Todos", "Sim", "Não"])

# Aplicar filtros
if tipo_selecionado != "Todos":
    df = df[df['tipo'] == tipo_selecionado]
if conector_selecionado != "Todos":
    df = df[df['conector'] == conector_selecionado]
if patrocinado_selecionado != "Todos":
    df = df[df['patrocinado'] == (1 if patrocinado_selecionado == "Sim" else 0)]

# Exibir dados filtrados
st.subheader("Dados Filtrados")
st.write(df)

# Análise de Preços
st.subheader("Análise de Preços")
fig_preco = px.histogram(df, x="preco", nbins=20, title="Distribuição de Preços")
st.plotly_chart(fig_preco)

# Média de preços
media_preco = df['preco'].mean()
st.write(f"Média de preços: R$ {media_preco:.2f}")

# Análise de Avaliações
st.subheader("Análise de Avaliações")
fig_avaliacao = px.histogram(df, x="avaliacao", nbins=5, title="Distribuição de Avaliações")
st.plotly_chart(fig_avaliacao)

# Média de avaliações
media_avaliacao = df['avaliacao'].mean()
st.write(f"Média de avaliações: {media_avaliacao:.1f} estrelas")

# Produtos Destacados
st.subheader("Produtos Destacados")
if 'nome' in df.columns:
    produto_mais_caro = df.loc[df['preco'].idxmax()]
    produto_mais_barato = df.loc[df['preco'].idxmin()]

    st.write(f"**Produto mais caro:** {produto_mais_caro['nome']} - R$ {produto_mais_caro['preco']:.2f}")
    st.write(f"**Produto mais barato:** {produto_mais_barato['nome']} - R$ {produto_mais_barato['preco']:.2f}")
else:
    st.warning("A coluna 'nome' não foi encontrada no banco de dados. Verifique o scraper.")

# Produtos Patrocinados
st.subheader("Produtos Patrocinados")
produtos_patrocinados = df[df['patrocinado'] == 1]
st.write(produtos_patrocinados)

# Links dos Produtos
st.subheader("Links dos Produtos")
for _, row in df.iterrows():
    st.write(f"[{row['nome']}]({row['link']})")