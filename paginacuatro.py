from selenium.webdriver.common.by import By

class Cuarta_Pagina:

    def __init__(self,driver):
        self.driver = driver

    nusuario = (By.NAME, "userName")
    crearu = (By.CSS_SELECTOR, "button[class='rounded-lg border font-medium px-6 disabled:bg-gray-100 disabled:text-gray-400 disabled:cursor-default text-white bg-color3 hover:bg flex items-center justify-center w-full h-[42px] mt-12']")

    def NusuarioItems(self):
        return self.driver.find_element(*Cuarta_Pagina.nusuario)
    
    def CrearuItems(self):
        return self.driver.find_element(*Cuarta_Pagina.crearu)