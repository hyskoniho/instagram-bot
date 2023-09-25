from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import random

class InstagramBot:
    def __init__(self, username, senha, hashtag):
        self.username = username
        self.senha = senha
        self.hashtag = hashtag
        self.driver = webdriver.Chrome(executable_path=r'D:\Projetos\InstagramBot\chromedriver117.exe')
    
    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")

        campo_username = WebDriverWait(driver, 120).until(EC.presence_of_element_located(('name', 'username')))
        campo_username.clear()
        campo_username.send_keys(username)

        campo_senha = driver.find_element('name', 'password')
        campo_senha.clear()
        campo_senha.send_keys(senha)
        campo_senha.send_keys(Keys.RETURN)

        time.sleep(10)

        self.curtir(hashtag)


    def curtir(self, hashtag):
        driver = self.driver
        listaLinks = []
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(10)

        for i in range(3):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(random.randint(10, 20))

        listaHrefs = driver.find_elements("tag name", "a")
        foto_href = [elem.get_attribute('href') for elem in listaHrefs]
        [href for href in foto_href if hashtag in href]

        for link in foto_href:
            try:
                if link.index("/p/") != -1:
                    listaLinks.append(link)
            except:
                pass

        for pic_href in listaLinks:
            driver.get(pic_href)
            driver.execute_script("scrollBy(0,100);")

            time.sleep(5)
            
            try:
                botaoCurtir = WebDriverWait(driver, 120).until(EC.presence_of_element_located(('class name', 'xp7jhwk')))
                botaoCurtir.click()
        
                time.sleep(random.randint(3, 5))
            except Exception as e:
                print(e)
                time.sleep(5)


username = input("Username: @")
senha = input("Senha: ")
hashtag = input("Hashtag: #")


bot = InstagramBot(username, senha, hashtag)
bot.login()