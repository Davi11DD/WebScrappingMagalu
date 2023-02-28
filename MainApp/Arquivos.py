from bs4 import BeautifulSoup
import re

class Arquivo : 
    oi =11
    def __init__(self, produto_nome) :
        self.produto_nome = produto_nome
        self.sopa = ''
        open(f'./DadosColetados/{produto_nome}.txt', 'w', encoding="UTF-8")


    def adicionarProdutos(self, grade_de_produtos, pagina) :
        self.sopa = BeautifulSoup(grade_de_produtos, 'html.parser')
        lista_produtos = self.sopa.find_all('li')
        arquivo = open(f'./DadosColetados/{self.produto_nome}.txt', 'a', encoding="UTF-8")

        arquivo.write(f'\n\n\n=============================== # PAGINA {pagina} # =====================================\n\n\n')

        for produto in lista_produtos :
            nome =  str(produto.find(attrs={'data-testid': 'product-title'}).text)
            preco = str(produto.find(attrs={'data-testid': 'price-value'  }).text)
            link =  str(produto.find('a').get('href'))

            print(nome)
            print(preco)
            print('https://www.magazineluiza.com.br'+link)


            arquivo.write(nome+'\n')
            arquivo.write(preco+'\n')
            arquivo.write('https://www.magazineluiza.com.br'+link+'\n\n')


