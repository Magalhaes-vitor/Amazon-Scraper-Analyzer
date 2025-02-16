import pytest
from scraper import criar_banco_dados, categorizar_fone, inserir_dados
import sqlite3

# Teste para verificar a criação do banco de dados
def test_criar_banco_dados():
    criar_banco_dados()
    conn = sqlite3.connect('amazon_fones.db')
    cursor = conn.cursor()
    
    # Verificar se as tabelas foram criadas
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tabelas = cursor.fetchall()
    assert ('fones',) in tabelas
    assert ('tipos',) in tabelas
    assert ('conectores',) in tabelas
    
    conn.close()

# Teste para verificar a categorização de fones
def test_categorizar_fone():
    descricao = "Fone Bluetooth com conector USB-C"
    tipo, conector = categorizar_fone(descricao)
    assert tipo == "Bluetooth"
    assert conector == "USB-C"

# Teste para verificar a inserção de dados
def test_inserir_dados():
    criar_banco_dados()
    inserir_dados("Bluetooth", "USB-C", "Fone Teste", 99.99, 4.5, "http://teste.com", 0, "2023-10-01 12:00:00")
    
    conn = sqlite3.connect('amazon_fones.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM fones WHERE nome = 'Fone Teste'")
    resultado = cursor.fetchone()
    
    assert resultado is not None
    assert resultado[2] == "Bluetooth"
    assert resultado[3] == "USB-C"
    assert resultado[4] == "Fone Teste"
    assert resultado[5] == 99.99
    
    conn.close()

# Executar os testes
if __name__ == "__main__":
    pytest.main()
