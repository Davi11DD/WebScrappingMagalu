from bs4 import BeautifulSoup
import re

class ensopar:


    def __init__(self, sopa, nome, pagina):
        self.pagina = pagina
        self.sopa = BeautifulSoup(sopa, 'html.parser')
        self.nome = nome
        

    def criarArquivo(nome) :
        open(f'./DadosColetados/{nome}.txt', 'w', encoding='UTF-8')
            

    def pegarProdutos(self) :   
        campoProdutos = self.sopa.find(attrs={'data-testid': 'product-list'})
        produtos = campoProdutos.find('ul').find_all('li')
        print(f'\033[1;32m{self.pagina}\033[m\n')
        arquivoA.write(f'{self.pagina}\n') 

        for c in produtos: 
            arquivoA = open(f'./DadosColetados/{self.nome}.txt', 'a', encoding='UTF-8')
            texto = c.find(attrs={'data-testid': 'product-title'}).text
            print(texto)
            preco = c.find(attrs={'data-testid': 'price-value'}).text
            print(preco+'\n')

            arquivoA.write(f'{texto}\n')     
            arquivoA.write(f'{preco}\n\n')

        




