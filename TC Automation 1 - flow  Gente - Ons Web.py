
# Pruebas Automaticas

#Nombre: Miguel Arango
#Versión: 3
#Fecha: 02/10/2024
#Descripción: Escenario flow "Geente" Web pag ONS


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
driver.find_element(By.LINK_TEXT, "Gente").click()

time.sleep(5)
dropdown = Select(driver.find_element(By.ID, "distance"))
dropdown.select_by_value("ciudad")
dropdown = Select(driver.find_element(By.ID, "id_province"))
dropdown.select_by_value("8")
dropdown = Select(driver.find_element(By.ID, "his_age"))
dropdown.select_by_value("25a35")
dropdown = Select(driver.find_element(By.ID, "her_age"))
dropdown.select_by_value("25a35")
dropdown = Select(driver.find_element(By.ID, "relationship"))
dropdown.select_by_value("noamigos")

time.sleep(5)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

time.sleep(5)
driver.find_element(By.ID, "is_compatible").click()

time.sleep(5)
driver.find_element(By.ID, "looking_for_256").click()
driver.find_element(By.ID, "looking_for_1024").click()
driver.find_element(By.ID, "looking_for_8").click()
driver.find_element(By.ID, "looking_for_1").click()

time.sleep(5)
driver.find_element(By.ID, "for_1").click()
driver.find_element(By.ID, "for_4096").click()
driver.find_element(By.ID, "for_8").click()
driver.find_element(By.ID, "for_4").click()
driver.find_element(By.ID, "for_128").click()

time.sleep(5)
driver.find_element(By.ID, "do_filter").click()

time.sleep(20)
driver.close()
print(driver.title)
print(driver.current_url)









