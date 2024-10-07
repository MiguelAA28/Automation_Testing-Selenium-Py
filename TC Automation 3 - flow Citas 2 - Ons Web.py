# Pruebas Automaticas

#Nombre: Miguel Arango
#Versión: 1
#Fecha: 08/10/2024
#Descripción: Escenario flow "Citas - Encontrar a alguien para quedar" Web pag ONS



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

time.sleep(10)
dropdown = Select(driver.find_element(By.ID, "date_in_region"))
dropdown.select_by_visible_text("")
dropdown = Select(driver.find_element(By.ID, "date_in_province"))
dropdown.select_by_visible_text("")

time.sleep(5)
driver.find_element(By.ID, "do_filter").click()

time.sleep(5)
driver.find_element(By.LINK_TEXT, "").click()


time.sleep(20)
driver.close()