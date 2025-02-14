import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime

# Função para criar o banco de dados e a tabela
def criar_banco_dados():
    conn = sqlite3.connect('amazon_fones.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS fones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,
            conector TEXT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            avaliacao REAL,
            link TEXT NOT NULL,
            patrocinado INTEGER DEFAULT 0,
            data_coleta TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Função para inserir dados no banco de dados
def inserir_dados(tipo, conector, nome, preco, avaliacao, link, patrocinado, data_coleta):
    conn = sqlite3.connect('amazon_fones.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO fones (tipo, conector, nome, preco, avaliacao, link, patrocinado, data_coleta)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (tipo, conector, nome, preco, avaliacao, link, patrocinado, data_coleta))
    conn.commit()
    conn.close()

# Função para determinar o tipo e o conector do fone
def categorizar_fone(descricao):
    descricao = descricao.lower()
    tipo = ""
    conector = ""

    if "bluetooth" in descricao:
        tipo = "Bluetooth"
    elif "headset" in descricao:
        tipo = "Headset"
    elif "intra-auricular" in descricao or "intra auricular" in descricao:
        tipo = "Intra-auricular"
    else:
        tipo = "Com cabo"

    if "p2" in descricao or "3.5mm" in descricao:
        conector = "P2"
    elif "usb-c" in descricao or "type-c" in descricao:
        conector = "USB-C"

    return tipo, conector

# Função para fazer o scraping das páginas da Amazon
def fazer_scraping():
    base_url = "https://www.amazon.com.br"
    search_query = "fones"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    for page in range(1, 6):  # Coletar as 5 primeiras páginas
        url = f"{base_url}/s?k={search_query}&page={page}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        produtos = soup.find_all('div', {'data-component-type': 's-search-result'})

        for produto in produtos:
            try:
                # Extrair informações do produto
                nome = produto.find('h2').text.strip()  # Nome do produto
                link = base_url + produto.find('a', {'class': 'a-link-normal'})['href']
                preco = produto.find('span', {'class': 'a-price-whole'})
                preco = float(preco.text.replace('.', '').replace(',', '.')) if preco else 0.0
                avaliacao = produto.find('span', {'class': 'a-icon-alt'})
                avaliacao = float(avaliacao.text.split()[0].replace(',', '.')) if avaliacao else 0.0
                patrocinado = 1 if produto.find('span', {'class': 'a-color-secondary'}) else 0

                # Categorizar o fone
                tipo, conector = categorizar_fone(nome)

                # Inserir dados no banco de dados
                data_coleta = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                inserir_dados(tipo, conector, nome, preco, avaliacao, link, patrocinado, data_coleta)
            except Exception as e:
                print(f"Erro ao processar produto: {e}")

# Executar o scraping e armazenar os dados
if __name__ == '__main__':
    criar_banco_dados()
    fazer_scraping()
    print("Dados coletados e armazenados com sucesso!")