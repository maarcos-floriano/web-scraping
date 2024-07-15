from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import requests
from bs4 import BeautifulSoup
import pandas as pd

app = Flask(__name__)

def buscar_produtos(termo):
    url = f'https://lista.mercadolivre.com.br/{termo}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    return soup

def extrair_informacoes(soup):
    produtos = []
    items = soup.find_all('div', {'class': 'ui-search-result__wrapper'})
    
    for item in items:
        titulo = item.find('h2', {'class': 'ui-search-item__title'}).text
        link = item.find('a', {'class': 'ui-search-link'})['href']
        preco = item.find('span', {'class': 'andes-money-amount__fraction'}).text
        
        produtos.append({
            'titulo': titulo,
            'link': link,
            'preco': preco
        })
        
    return produtos

def salvar_csv(produtos, nome_arquivo):
    df = pd.DataFrame(produtos)
    df.to_csv(nome_arquivo, index=False, encoding='utf-8')
    print(f'Arquivo {nome_arquivo} salvo com sucesso!')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    termo = request.form['termo']
    soup = buscar_produtos(termo)
    produtos = extrair_informacoes(soup)
    return render_template('index.html', produtos=produtos, termo=termo)

if __name__ == '__main__':
    app.run(debug=True)
