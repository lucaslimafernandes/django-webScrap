from django.test import TestCase

# Create your tests here.
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ["PATH"] += os.pathsep + os.path.join(BASE_DIR,'/gecko')

from django.test import LiveServerTestCase
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary



class AccountTestCase(LiveServerTestCase):
    def test_login(self):

        #binary = FirefoxBinary('/Lucas/Selenium/gecko')
        #driver = webdriver.Firefox(firefox_binary=binary)
        driver = webdriver.Firefox()
        driver.get('http://google.com')
        #username = driver.find_element_by_id('id_username')
        #password = driver.find_element_by_id('id_password')
        #submit = driver.find_element_by_tag_name('button')
        #username.send_keys('superusername')
        #password.send_keys('superuserpassword')
        #submit.send_keys(Keys.RETURN)

    
def busca_zoom(item):
    url = f'https://www.zoom.com.br/search?q={item}'

    #Acesso browser
    #browser = webdriver.Chrome() #Caso use Windows, deixar o webdriver na mesma pasta do script e usar esta variavel
    #browser = webdriver.Chrome('/usr/local/bin/chromedriver') #Caso use Linux -- instalar o webdriver sudo mv -f chromedriver /usr/local/bin/chromedriver
    
    browser = webdriver.Firefox()
    
    browser.get(url)
    browser.maximize_window()

    nomes = browser.find_elements_by_xpath("//span[@class='Cell_Name__jnsS-']")
    preco = browser.find_elements_by_xpath("//strong[@class='Text_Text___RzD- Text_LabelMdBold__3KBIj CellPrice_MainValue__3s0iP']")

    listNomes = [i.text for i in nomes]
    listPreco = [i.text for i in preco]

    return {'nome': listNomes, 'preco':listPreco}

    #for i in range(0, len(listNomes)):
    #    print(f'Produto: {listNomes[i]} - {listPreço[i]}')

