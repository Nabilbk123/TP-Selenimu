import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless") # Ensure GUI is off
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(2) #Pour donner le temps de s'afficher / Si on l'uti#
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.CLASS_NAME,"oxd-button").click()
time.sleep(2)

driver.find_element(By.CLASS_NAME,"oxd-text").is_displayed()
Dashbord=driver.find_element(By.CLASS_NAME,"oxd-topbar-header-breadcrumb-module").text
print(Dashbord)
time.sleep(5)
driver.close()