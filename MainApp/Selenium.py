from Sopa import ensopar
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service
chormeServices = Service(ChromeDriverManager().install())

# chromeOptions.add_argument('--headless')



class catchar:

    def __init__(self, produto):
        chromeOptions = Options()
        chromeOptions.add_argument('--window-size=800,600')
        chromeOptions.add_argument('--window-position=0,0')

        driver = webdriver.Chrome(service=chormeServices, options=chromeOptions)
        driver.implicitly_wait(11)
        driver.get('https://www.magazineluiza.com.br/')
    
        input_search = driver.find_element(By.XPATH, '//*[@id="input-search"]')
        input_search.send_keys(f'{produto}')   
        input_search.submit()
        
        ensopar.criarArquivo(nome=produto)

        
        for c in range(1, 12) :
            sleep(2)

            grade_de_produtos = driver.find_element(By.CSS_SELECTOR, '[data-testid="product-list"]')

            sopa = ensopar(grade_de_produtos.get_attribute('outerHTML'), produto, c)
            sopa.pegarProdutos()

        
            navigation = driver.find_element( By.XPATH, '//*[@id="__next"]/div/main/section[4]/div[4]/nav')
            botaoNext = navigation.find_elements( By.TAG_NAME, 'li')[-1].find_element(By.TAG_NAME, 'button')
            try:            
                driver.execute_script('arguments[0].click()', botaoNext)
            
            except: break
            



        
