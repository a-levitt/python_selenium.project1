import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.maximize_window()

driver.find_element(By.NAME, "username").send_keys("Admin")

driver.find_element(By.NAME, "password").send_keys("admin123")

driver.find_element(By.XPATH, "//button[@type='submit']").click()

driver.find_element(By.CLASS_NAME, "oxd-userdropdown-tab").click()

driver.find_element(By.LINK_TEXT, "Logout").click()

time.sleep(5)

driver.back()

time.sleep(10)

driver.close()
