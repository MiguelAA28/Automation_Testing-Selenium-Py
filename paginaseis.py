from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Sexta_Pagina:

    def validate_multiple_texts(self, driver, selectors_and_texts, wait):

        self.driver = driver
        wait = WebDriverWait(driver, 15)
        selectors_and_texts = [((By.XPATH, "//p[text()='Al menos 8 caracteres']"), "Al menos 8 caracteres"), ((By.XPATH, "//p[text()='Al menos 1 minúscula']"), "Al menos 1 minúscula"), ((By.XPATH, "//p[text()='Al menos 1 mayúscula']"), "Al menos 1 mayúscula")]

        for selector, expected_text in selectors_and_texts:
            elemento = wait.until(EC.presence_of_element_located(selector))
            assert elemento.text == expected_text, f"Texto esperado: '{expected_text}', pero se encontró: '{elemento.text}'"

        print("Todos los textos esperados han sido validados correctamente.")





    