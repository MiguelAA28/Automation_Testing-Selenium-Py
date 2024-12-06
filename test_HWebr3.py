from utilities import Clase_Base 
from paginauno import Pagina_Inicio
from paginados import Segunda_Pagina
from paginatres import Tercera_Pagina
from paginaseis import Sexta_Pagina
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pytest
import time

@pytest.mark.usefixtures("setup")

class TestTres(Clase_Base):
    
    def test_ph(self, setup):
        driver = setup

        time.sleep(5)
        paginainicial = Pagina_Inicio(driver)
        paginainicial.InicialItems().click()

        time.sleep(5)
        paginasecundaria = Segunda_Pagina(driver)
        paginasecundaria.SegundosItems().click()

        time.sleep(5)
        paginaterciaria = Tercera_Pagina(driver)
        paginaterciaria.UsuarioItems().send_keys("m.a.a.arango@hotmail.com")
        paginaterciaria = Tercera_Pagina(driver)
        paginaterciaria.ContraseñaItems().send_keys("Prueba12345")

        vista = Sexta_Pagina()
        wait = WebDriverWait(driver, 15)
        selectors_and_texts = [((By.XPATH, "//p[text()='Al menos 8 caracteres']"), "Al menos 8 caracteres"), ((By.XPATH, "//p[text()='Al menos 1 minúscula']"), "Al menos 1 minúscula"), ((By.XPATH, "//p[text()='Al menos 1 mayúscula']"), "Al menos 1 mayúscula")]

        vista.validate_multiple_texts(driver, selectors_and_texts, wait)

        time.sleep(5)
        driver.close()