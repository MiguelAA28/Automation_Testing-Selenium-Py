from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Octava_Pagina:
    def __init__(self, driver):
        self.driver = driver
        self.mensaje_selector = "span.text-sm.text-red-500.mt-1"

    def obtener_mensajes(self, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.mensaje_selector))) 
    
    def validar_mensajes_condicional(self, email):
        mensajes = [mensaje.text for mensaje in self.obtener_mensajes()]

        if not email:  
            assert any("Parece que aun no tienes una cuenta creada" in mensaje for mensaje in mensajes), "El mensaje esperado 'Parece que aun no tienes una cuenta creada' no se encontró."
        
        elif "@" not in email:  
            assert any("Parece que el email esta incompleto" in mensaje for mensaje in mensajes), "El mensaje esperado 'Parece que el email esta incompleto' no se encontró."
        