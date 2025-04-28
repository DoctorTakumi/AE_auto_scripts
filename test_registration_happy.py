from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# relative path for the chromedriver
service_obj = Service ("./chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# navigating to the provided link (sign in)
driver.get("https://lemon-cliff-03b907503.6.azurestaticapps.net/")
time.sleep(2)

# toggling to chosen language (EN)
driver.find_element(By.XPATH, "//button[text()='EN']").click()
time.sleep(2)

# clicking Register button to navigate to the Registration widget
driver.find_element(By.XPATH, "//a[text()='Register']").click()

# entering First and Last Name
driver.find_element(By.XPATH, "//input[@aria-label='firstAndLastName']").send_keys("Test")
time.sleep(2)

# entering Email
driver.find_element(By.XPATH, "//input[@aria-label='email']").send_keys("testnirachun1208+04@gmail.com")
time.sleep(2)


# password section - I added eye toggle on and off before and after entering the password
# if not needed - comment out
password_eye_button = driver.find_element(By.XPATH, "(//div[@role='button' and @aria-label='eyeopen'])[1]")
password_eye_button.click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@aria-label='password']").send_keys("Password321!")
time.sleep(2)
password_eye_button.click()
time.sleep(1)


# confirm password section - I added eye toggle on and off before and after entering the repeated password
# if not needed - comment out
confirm_password_eye_button = driver.find_element(By.XPATH, "(//div[@role='button' and @aria-label='eyeopen'])[2]")
confirm_password_eye_button.click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@aria-label='confirmPassword']").send_keys("Password321!")
time.sleep(2)
confirm_password_eye_button.click()
time.sleep(1)

# final registration
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)


# final register confirmation
# Wait until the URL is the expected full sign-in URL
WebDriverWait(driver, 10).until(EC.url_to_be("https://lemon-cliff-03b907503.6.azurestaticapps.net/auth/sign-in"))

# Assert that the current URL is exactly correct
assert driver.current_url == "https://lemon-cliff-03b907503.6.azurestaticapps.net/auth/sign-in"