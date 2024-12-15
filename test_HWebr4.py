from paginasiete import Septima_Pagina
from paginaocho import Octava_Pagina
from paginados import Segunda_Pagina
from paginauno import Pagina_Inicio
from utilities import Clase_Base 
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
        paginaterciaria = Septima_Pagina(driver)
        email = ""
        paginaterciaria.UsuarioItems().send_keys(email)

        time.sleep(5)
        paginaoctava = Octava_Pagina(driver)
        paginaoctava.validar_mensajes_condicional(email)
        
        time.sleep(5)
        driver.close()