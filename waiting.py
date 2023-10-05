from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://casenik.com.ua/user/login")

login_field = driver.find_element(By.XPATH, '//input[@id="email"]')
login_field.send_keys("xotrecroummabru-7139@yopmail.com")
password_field = driver.find_element(By.XPATH, '//input[@id="pasword"]')
password_field.send_keys("mabru-7139")
login_button = driver.find_element(By.XPATH, '//button[@class="btn button-gen"]')
login_button.click()

message = WebDriverWait(driver, 29).until_not(
    EC.visibility_of_element_located((By.XPATH, "//div[@class = 'alert alert-success']"))
    )


time.sleep(5)




