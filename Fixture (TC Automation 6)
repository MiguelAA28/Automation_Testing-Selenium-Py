import time
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Browser name to run tests: chrome or firefox"
    )

@pytest.fixture
def setup(request):
    browser_name = request.config.getoption("browser_name")
    
    if browser_name == "chrome":
        driver = webdriver.Chrome()  
    elif browser_name == "firefox":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Navegador '{browser_name}' no soportado.")
    
    driver.get("http://localhost:5173/")
    driver.maximize_window()
    time.sleep(5)
    yield driver
    driver.quit()

