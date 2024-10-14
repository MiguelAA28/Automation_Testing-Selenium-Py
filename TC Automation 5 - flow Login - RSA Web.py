# Pruebas Automaticas

#Nombre: Miguel Arango
#Versión: 2
#Fecha: 14/10/2024
#Descripción: Validación mensaje de error en login, RSA Web


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
import time

Service = webdriver.ChromeService()
driver = webdriver.Chrome(service = Service)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()

time.sleep(5)
driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()
windowsOpened = driver.window_handles

time.sleep(5)
driver.switch_to.window(windowsOpened[1])
message = driver.find_element(By.CSS_SELECTOR, ".red").text
var = message.split("at")[1].strip().split(" ")[0]

time.sleep(5)
driver.close()
driver.switch_to.window(windowsOpened[0])

time.sleep(5)
driver.find_element(By.NAME, "username").send_keys("rahulshettyacademy")
driver.find_element(By.NAME, "password").send_keys("learnin")
driver.find_element(By.ID, "terms").click()

time.sleep(10)
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)

time.sleep(5)
driver.close()