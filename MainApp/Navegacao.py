# IMPORTS -----------------------------------------------------------
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by   import By

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from time import sleep
from Arquivos import Arquivo
import re

#====================================================================
# Config Iniciais ---------------------------------------------------
chromeService = Service(ChromeDriverManager().install())

chromeOptions = Options()
chromeOptions.add_argument('--window-size=800,600')
chromeOptions.add_argument('--window-position=0,0')

#====================================================================
# Produto e Preferências --------------------------------------------


class Selenium :
    def __init__(self, produto_nome, visibilidade) :
        

        if visibilidade in 'N n Nao NAO NÃO não' : chromeOptions.add_argument('--headless')

        #====================================================================
        # DRIVER ------------------------------------------------------------
        arquivo = Arquivo(produto_nome)

        driver = webdriver.Chrome(service=chromeService, options=chromeOptions)
        driver.implicitly_wait(11)
        driver.get('https://www.magazineluiza.com.br')

        # ===================================================================
        # CÒDIGO ------------------------------------------------------------
        input_de_procura = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="input-search"]')
        input_de_procura.send_keys(f'{produto_nome}')
        input_de_procura.submit()

        sleep(2)

        pagina = 1 
        url = ''
        while True :

            if url != driver.current_url :

                print(f'\033[1;32mPagina\033[m {pagina}\n')

                grade_de_produtos = driver.find_element(By.CSS_SELECTOR, 'div[data-testid="product-list"]').find_element(By.TAG_NAME, 'ul')
                arquivo.adicionarProdutos(grade_de_produtos.get_attribute('outerHTML'), pagina)

                url = driver.current_url
                sleep(1.5)
                grade_de_paginas = driver.find_element(By.CSS_SELECTOR, 'nav[aria-label="pagination navigation"]').find_element(By.TAG_NAME, 'ul')
                botao_next = grade_de_paginas.find_element(By.CSS_SELECTOR, 'button[aria-label="Go to next page"]')
                driver.execute_script('arguments[0].click()', botao_next)
                
                pagina += 1

            if pagina == 12 : break

        print('\033[1;32m ------------------- FIM --------------------\033[m')

        driver.quit()
        driver.close()



# =================================================================== FIM :)