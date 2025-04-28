from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# adding the function to use the current time in seconds so every time script is executed email is different so we won't get duplication error
# madefor the easier script maintenance
# if not needed - comment out and use driver.find_element(By.XPATH, "//input[@aria-label='email']").send_keys([enter email here]) instead of calling the function
def get_next_email():
    timestamp = int(time.time())  # Get current time in seconds
    email = f"testnirachun1208+{timestamp}@gmail.com"
    return email


# relative path for the chromedriver
service_obj = Service ("./chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# navigating to the provided link (sign in)
driver.get("https://lemon-cliff-03b907503.6.azurestaticapps.net/")

# waiting for the page load for the element to become clickable
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='EN']")))
# toggling to chosen language (EN)
driver.find_element(By.XPATH, "//button[text()='EN']").click()

# waiting for the Register link to be clickable
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Register']")))
# clicking Register button to navigate to the Registration widget
driver.find_element(By.XPATH, "//a[text()='Register']").click()

# waiting for the first input field is visible
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='firstAndLastName']")))
# entering First and Last Name
driver.find_element(By.XPATH, "//input[@aria-label='firstAndLastName']").send_keys("Test")


# calling the above written function to generate new email based on current time in seconds
email = get_next_email()
driver.find_element(By.XPATH, "//input[@aria-label='email']").send_keys(email)

# entering Email - use if function above is not needed
# driver.find_element(By.XPATH, "//input[@aria-label='email']").send_keys("testnirachun1208+06@gmail.com")


# password section - I added eye toggle on and off before and after entering the password
# if not needed - comment out
password_eye_button = driver.find_element(By.XPATH, "(//div[@role='button' and @aria-label='eyeopen'])[1]")
password_eye_button.click()
time.sleep(1)

driver.find_element(By.XPATH, "//input[@aria-label='password']").send_keys("Password321!")
time.sleep(1)

password_eye_button.click()
time.sleep(1)


# confirm password section - I added eye toggle on and off before and after entering the repeated password
# if not needed - comment out
confirm_password_eye_button = driver.find_element(By.XPATH, "(//div[@role='button' and @aria-label='eyeopen'])[2]")
confirm_password_eye_button.click()
time.sleep(1)

driver.find_element(By.XPATH, "//input[@aria-label='confirmPassword']").send_keys("Password321!")
time.sleep(1)

confirm_password_eye_button.click()
time.sleep(1)

# final registration
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# final register confirmation
# Wait until the URL is the expected full sign-in URL
WebDriverWait(driver, 10).until(EC.url_to_be("https://lemon-cliff-03b907503.6.azurestaticapps.net/auth/sign-in"))

# Assert that the current URL is exactly correct
assert driver.current_url == "https://lemon-cliff-03b907503.6.azurestaticapps.net/auth/sign-in"