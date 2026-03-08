#Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.linkedin.com/login/")#

wait = WebDriverWait(driver, 10)

# Wait for username field to be visible and enter value
username = wait.until(EC.visibility_of_element_located((By.ID, "username")))
username.send_keys("xxxx@gmail.com")

# Password field
password = driver.find_element(By.ID, "password")
password.send_keys("S*********@123")

# Submit login
password.send_keys(Keys.ENTER)

# Wait some time for login to complete
time.sleep(20)

print("Logged in successfully")

driver.quit()
