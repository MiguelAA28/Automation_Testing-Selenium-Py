
# Pruebas Automaticas

#Nombre: Miguel Arango
#Versión: 2
#Fecha: 06/10/2024
#Descripción: Escenario flow "Citas - publicar tu anuncio para quedar" Web pag ONS



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://es.onswingers.com/")
driver.maximize_window()

time.sleep(5)
driver.find_element(By.CLASS_NAME, "cm-btn-accept-all").click()
driver.find_element(By.NAME, "username").send_keys("")
driver.find_element(By.ID, "password").send_keys("")

time.sleep(10)
driver.find_element(By.ID, "do_login").click()
driver.find_element(By.LINK_TEXT, "Citas").click()

time.sleep(5)
driver.find_element(By.ID, "create_date").click()

time.sleep(10)
dropdown = Select(driver.find_element(By.ID, "when"))
dropdown.select_by_visible_text("")
dropdown = Select(driver.find_element(By.ID, "for_days"))
dropdown.select_by_visible_text("")
dropdown = Select(driver.find_element(By.ID, "id_province"))
dropdown.select_by_visible_text("")
dropdown = Select(driver.find_element(By.ID, "id_city"))
dropdown.select_by_visible_text("")
dropdown = Select(driver.find_element(By.ID, "looking_for"))
dropdown.select_by_visible_text("")
driver.find_element(By.ID, "description").send_keys("")

time.sleep(5)
driver.find_element(By.ID, "submit_form").click()

time.sleep(7)
mensaje_exito = driver.find_element(By.XPATH, "//h4[text() = 'Tu anuncio para quedar se ha publicado con éxito.']")

if 'Tu anuncio para quedar se ha publicado con éxito.' in mensaje_exito.text:
        print("Test exitoso: El formulario se envió correctamente.")




time.sleep(20)
driver.close()
