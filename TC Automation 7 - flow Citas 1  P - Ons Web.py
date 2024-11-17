# Pruebas Automaticas

#Nombre: Miguel Arango
#Versión: 3
#Fecha: 14/11/2024
#Descripción: Escenario flow "Gente" - Performado Web pag ONS

from utilitieso import Clase_Principal
from ventanaemerg import Pop_Up
from loginpg import Pg_Login
from gentepagi import Pg_Gente
from dropdwn import Pg_Dropdw
from compatibilipg import Pg_Compati
from busquedapg import Pg_Busqueda
from objetivpg import Pg_Objetiv
from botonpg import Execut_Busque
import pytest
import time

@pytest.mark.usefixtures("my_setup")

class TestOns(Clase_Principal):

    def test_ons(self, my_setup):
        driver = my_setup

        popupmensaje = Pop_Up(driver)
        popupmensaje.MensajeItems().click()

        time.sleep(5)
        loginini = Pg_Login(driver)
        loginini.UsuarioItems().send_keys("")
        loginini = Pg_Login(driver)
        loginini.ContraseñaItems().send_keys("")
        loginini = Pg_Login(driver)
        loginini.LoginItems().click()

        time.sleep(5)
        vistagente = Pg_Gente(driver)
        vistagente.gentesItems().click()

        time.sleep(5)
        dropgente = Pg_Dropdw(driver)
        dropgente.DistanciaItems().select_by_value("")
        dropgente = Pg_Dropdw(driver)
        dropgente.ProvinciaItems().select_by_value("")
        dropgente = Pg_Dropdw(driver)
        dropgente.EdadelItems().select_by_value("")
        dropgente = Pg_Dropdw(driver)
        dropgente.EdadellaItems().select_by_value("")
        dropgente = Pg_Dropdw(driver)
        dropgente.RelacionItems().select_by_value("")
        
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        time.sleep(5)
        compatigente = Pg_Compati(driver)
        compatigente.CompatibleItems().click()

        time.sleep(5)
        busquedagente = Pg_Busqueda(driver)
        busquedagente.HeterItems().click()
        busquedagente = Pg_Busqueda(driver)
        busquedagente.BixualItems().click()
        busquedagente = Pg_Busqueda(driver)
        busquedagente.HetermuItems().click()
        busquedagente = Pg_Busqueda(driver)
        busquedagente.HeterhoItems().click()

        time.sleep(5)
        objetivgente = Pg_Objetiv(driver)
        objetivgente.InterunoItems().click()
        objetivgente = Pg_Objetiv(driver)
        objetivgente.InterdosItems().click()
        objetivgente = Pg_Objetiv(driver)
        objetivgente.IntertresItems().click()
        objetivgente = Pg_Objetiv(driver)
        objetivgente.IntercuatroItems().click()
        objetivgente = Pg_Objetiv(driver)
        objetivgente.IntercincoItems().click()
        
        time.sleep(5)
        busqueda = Execut_Busque(driver)
        busqueda.BotonItems().click()

        print(driver.title)
        print(driver.current_url)
        driver.close()
