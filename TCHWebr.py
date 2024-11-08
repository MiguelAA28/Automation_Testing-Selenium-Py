import time
from utilities import Clase_Base  
from paginauno import Pagina_Inicio
from paginados import Segunda_Pagina
from paginatres import Tercera_Pagina
from paginacuatro import Cuarta_Pagina

class TestUno(Clase_Base):

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

        time.sleep(5)
        paginaterciaria = Tercera_Pagina(driver)
        paginaterciaria.CrearItems().click()

        time.sleep(5)
        paginacuaternaria = Cuarta_Pagina(driver)
        paginacuaternaria.NusuarioItems().send_keys("PruebaMAAA5")

        time.sleep(5)
        paginacuaternaria = Cuarta_Pagina(driver)
        paginacuaternaria.CrearuItems().click()

        time.sleep(5)
        driver.get_screenshot_as_file("C:\\Users\\HP\\OneDrive\\Imágenes\\Capturas de pantalla\\ScreenShotHenrry1.png")

        time.sleep(5)
        driver.close()



        


