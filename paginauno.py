from selenium.webdriver.common.by import By

class Pagina_Inicio:

    def __init__(self,driver):
        self.driver = driver

    inicio = (By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(1) > header:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > button:nth-child(1)")

    def InicialItems(self):
        return self.driver.find_element(*Pagina_Inicio.inicio)
        
