import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
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