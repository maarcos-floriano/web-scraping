
# Web Scraping de Produtos do Mercado Livre

## Descrição

Este projeto realiza web scraping no site do Mercado Livre para buscar produtos com base em um termo fornecido pelo usuário, extrai informações como título, link e preço dos produtos encontrados e salva esses dados em um arquivo CSV usando a biblioteca `pandas`.

## Estrutura do Projeto

O projeto consiste em um script Python que executa as seguintes etapas principais:

1. **Buscar produtos no Mercado Livre**: Realiza uma requisição HTTP para obter a página de resultados de busca.
2. **Extrair informações dos produtos**: Analisa o HTML da página para extrair os dados desejados.
3. **Salvar os dados em um arquivo CSV**: Usa a biblioteca `pandas` para salvar as informações em um arquivo CSV.

## Requisitos

- Python 3.x
- Bibliotecas:
  - `requests`
  - `beautifulsoup4`
  - `lxml`
  - `pandas`

## Instalação

Instale as bibliotecas necessárias utilizando `pip`:

```bash
pip install requests beautifulsoup4 lxml pandas
```

## Uso

1. **Clonar o repositório** (se aplicável):
   ```bash
   git clone <URL-do-repositorio>
   cd <nome-do-repositorio>
   ```

2. **Executar o script**:
   ```bash
   python nome_do_script.py
   ```

3. **Entrar com o termo de busca**: Quando solicitado, digite o nome do produto que deseja buscar no Mercado Livre.

4. **Visualizar o arquivo CSV gerado**: O script salvará os dados em um arquivo CSV no diretório atual com um nome baseado no termo de busca fornecido.

## Estrutura do Código

### Importações

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
```

### Funções

#### 1. `buscar_produtos(termo)`

Realiza a busca no Mercado Livre para o termo fornecido.

- **Parâmetros**: 
  - `termo` (str): Termo de busca fornecido pelo usuário.
- **Retorno**: 
  - `soup` (BeautifulSoup): Objeto BeautifulSoup com o conteúdo da página de resultados de busca.

#### 2. `extrair_informacoes(soup)`

Extrai informações dos produtos da página de resultados.

- **Parâmetros**: 
  - `soup` (BeautifulSoup): Objeto BeautifulSoup com o conteúdo da página de resultados de busca.
- **Retorno**: 
  - `produtos` (list): Lista de dicionários com informações dos produtos (título, link, preço).

#### 3. `salvar_csv(produtos, nome_arquivo)`

Salva as informações dos produtos em um arquivo CSV usando pandas.

- **Parâmetros**: 
  - `produtos` (list): Lista de dicionários com informações dos produtos.
  - `nome_arquivo` (str): Nome do arquivo CSV a ser salvo.

### Função Principal

#### `main()`

Executa o fluxo principal do script.

- Solicita o termo de busca ao usuário.
- Chama as funções `buscar_produtos`, `extrair_informacoes` e `salvar_csv`.
- Salva os dados em um arquivo CSV com base no termo de busca fornecido.

### Código Completo

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Função para buscar produtos no Mercado Livre
def buscar_produtos(termo):
    url = f'https://lista.mercadolivre.com.br/{termo}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    return soup

# Função para extrair informações dos produtos
def extrair_informacoes(soup):
    produtos = []
    items = soup.find_all('div', {'class': 'ui-search-result__wrapper'})
    
    for item in items:
        titulo = item.find('h2', {'class': 'ui-search-item__title'}).text
        link = item.find('a', {'class': 'ui-search-link'})['href']
        preco = item.find('span', {'class': 'price-tag-fraction'}).text
        
        produtos.append({
            'titulo': titulo,
            'link': link,
            'preco': preco
        })
        
    return produtos

# Função para salvar as informações em um arquivo CSV usando pandas
def salvar_csv(produtos, nome_arquivo):
    df = pd.DataFrame(produtos)
    df.to_csv(nome_arquivo, index=False, encoding='utf-8')
    print(f'Arquivo {nome_arquivo} salvo com sucesso!')

# Função principal
def main():
    termo = input("Digite o nome do produto que deseja buscar: ")
    soup = buscar_produtos(termo)
    produtos = extrair_informacoes(soup)
    nome_arquivo = f'{termo.replace(" ", "_")}_mercadolivre.csv'
    salvar_csv(produtos, nome_arquivo)

if __name__ == '__main__':
    main()
```

## Notas Importantes

- **Política de Uso**: Certifique-se de cumprir a política de uso do site do Mercado Livre e não fazer muitas requisições em um curto período para evitar ser bloqueado.
- **Limitações**: Este script é uma versão básica de um scraper e pode precisar de ajustes para lidar com mudanças no layout do site ou para coletar informações adicionais.

## Contribuições

Contribuições são bem-vindas! Se você encontrar problemas ou tiver sugestões para melhorias, sinta-se à vontade para abrir um problema ou enviar um pull request.

## Licença

Este projeto está licenciado sob os termos da [MIT License](LICENSE).
