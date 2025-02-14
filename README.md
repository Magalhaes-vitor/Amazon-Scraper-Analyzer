# Amazon Scraper & Analyzer

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)

![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-orange)

![SQLite](https://img.shields.io/badge/SQLite-3.0%2B-green)

O **Amazon Scraper & Analyzer** é uma aplicação Python
que coleta dados de fones de ouvido da Amazon, categoriza-os por tipo
(Bluetooth, com cabo, headset, intra-auricular) e conector (P2, USB-C), e
armazena as informações em um banco de dados SQLite. Além disso, a aplicação
inclui uma interface interativa desenvolvida com Streamlit para análise e
visualização dos dados coletados, como preços, avaliações e produtos
patrocinados.

---

## Funcionalidades

- **Web Scraping**: Coleta de dados das 5 primeiras páginas
  de resultados da Amazon para a pesquisa por "fones".
- **Categorização Automática**: Classificação dos fones por
  tipo e conector com base na descrição do produto.
- **Armazenamento em Banco de Dados**: Dados organizados e
  armazenados em um banco de dados SQLite.
- **Análise Interativa**: Visualização de dados com gráficos
  e métricas usando Streamlit.

---

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **BeautifulSoup**: Biblioteca para web scraping.
- **SQLite**: Banco de dados para armazenamento dos dados
  coletados.
- **Streamlit**: Framework para criação da interface de
  análise de dados.
- **Pandas**: Manipulação e análise de dados.
- **Plotly**: Criação de gráficos interativos.

---

## Como Usar

### Pré-requisitos

Certifique-se de ter o Python 3.8 ou superior instalado.
Além disso, instale as dependências do projeto:

```bash



pip install -r requirements.txt



```

### Executando o Projeto

1. **Coleta de Dados**:

   - Execute o script
     `scraper.py` para coletar os dados da Amazon e armazená-los no banco de dados.

   ```bash



   python scraper.py



   ```
2. **Visualização e Análise**:

   - Execute a
     aplicação Streamlit para visualizar e analisar os dados coletados.

   ```bash



   streamlit run
   ```

app.py

```



 



   Isso abrirá uma
interface no navegador onde você poderá explorar os dados.



 



---



 



## Estrutura do Projeto



 



```

Amazon-Scraper-Analyzer/

├── scraper.py

# Script para coleta de dados

├── app.py

# Aplicação Streamlit para análise

├── amazon_fones.db

# Banco de dados SQLite

├── README.md

# Documentação do projeto

└── requirements.txt

# Lista de dependências

```



 



---



 



## Exemplo de Uso



 



1. **Coletar Dados**:



   - Execute o
`scraper.py` para coletar os dados da Amazon.



 



2. **Analisar Dados**:



   - Execute o
`app.py` e explore os dados coletados através da interface do Streamlit.



 



---



 



## Contribuição



 



Contribuições são bem-vindas! Siga os passos abaixo:



 



1. Faça um fork do repositório.



2. Crie uma branch para sua feature (`git checkout -b
feature/nova-feature`).



3. Commit suas mudanças (`git commit -m 'Adicionando nova
feature'`).



4. Faça push para a branch (`git push origin
feature/nova-feature`).



5. Abra um Pull Request.



 



---



 



## Licença



 



Este projeto está licenciado sob a licença MIT. Veja o
arquivo [LICENSE](LICENSE) para mais detalhes.



 



---



 



## Contato



 



Se tiver dúvidas ou sugestões, entre em contato:



 



- **Nome**: Vitor Magalhães



- **GitHub**:
[Magalhaes-vitor](https://github.com/Magalhaes-vitor)



- **Email**: vitor.magalhaes@example.com



- **Linkedin**: [Magalhaes-vitor]((https://www.linkedin.com/in/magalhaes-vitor/)



```

---

### Arquivo `requirements.txt`

Crie um arquivo `requirements.txt` para listar as
dependências do projeto:

```plaintext



requests==2.26.0



beautifulsoup4==4.10.0



pandas==1.3.4



streamlit==1.0.0



plotly==5.3.1



sqlite3==3.36.0



```

---

### Arquivo `LICENSE`

Adicione um arquivo `LICENSE` ao projeto para definir os
termos de uso. Aqui está um exemplo de licença MIT:

```plaintext



MIT License



 



Copyright (c) 2023 Vitor Magalhães



 



Permission is hereby granted, free of charge, to any person
obtaining a copy



of this software and associated documentation files (the
"Software"), to deal



in the Software without restriction, including without
limitation the rights



to use, copy, modify, merge, publish, distribute,
sublicense, and/or sell



copies of the Software, and to permit persons to whom the
Software is



furnished to do so, subject to the following conditions:



 



The above copyright notice and this permission notice shall
be included in all



copies or substantial portions of the Software.



 



THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY
OF ANY KIND, EXPRESS OR



IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY,



FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO
EVENT SHALL THE



AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER



LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM,



OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE



SOFTWARE.



```

---

### Como Publicar no GitHub

1. Crie um novo repositório no GitHub.
2. No terminal, navegue até a pasta do projeto e execute os
   seguintes comandos:

   ```bash



   git init



   git add .



   git commit -m
   ```

"Initial commit"

   git branch -M main

   git remote add
origin https://github.com/seu-usuario/nome-do-repositorio.git

   git push -u origin
main

```



 



3. Acesse o repositório no GitHub e confira se todos os
arquivos foram enviados.



 



---
```
