from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# function to assert error messages
def assert_text_present(driver, xpath, expected_text, test_name):
    try:
        error_text = driver.find_element(By.XPATH, xpath).text
        assert expected_text in error_text
        print(f"{test_name}: PASSED")
    except AssertionError:
        print(f"{test_name}: FAILED")

# function written to clear fields before new entries
def clear_and_type(driver, xpath, value):
    field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    field.clear()
    field.send_keys(value)

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

# ----------------------------------------------------------------------------------------------------------------------------------------
# FIRST SET OF ENTRIES - BLANK FIELDS
driver.find_element(By.XPATH, "//input[@aria-label='firstAndLastName']").send_keys("")
driver.find_element(By.XPATH, "//input[@aria-label='email']").send_keys("")
driver.find_element(By.XPATH, "//input[@aria-label='password']").send_keys("")
driver.find_element(By.XPATH, "//input[@aria-label='confirmPassword']").send_keys("")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)

# FIRST SET OF ASSERTIONS
# Assert First and Last Name required error
print ("First set of assertions - blank fields:")
assert_text_present(driver, "(//div[@class='ng-invalid-touched-feedback ng-star-inserted'])[1]", "Required", "Test 1 (Name and Last Name empty validation)")
assert_text_present(driver, "(//div[@class='ng-invalid-touched-feedback ng-star-inserted'])[2]", "Required", "Test 2 (Email empty validation)")
assert_text_present(driver, "(//div[@class='ng-invalid-touched-feedback ng-star-inserted'])[3]", "Required", "Test 3 (Password empty validation)")
assert_text_present(driver, "(//div[@class='ng-invalid-touched-feedback ng-star-inserted'])[4]", "Required", "Test 4 (Confirm Password empty validation)")
    

# ----------------------------------------------------------------------------------------------------------------------------------------    
# SECOND SET OF ENTRIES - INVALID INPUTS
driver.find_element(By.XPATH, "//input[@aria-label='email']").send_keys("test@")
driver.find_element(By.XPATH, "//input[@aria-label='password']").send_keys("12345")
driver.find_element(By.XPATH, "//input[@aria-label='confirmPassword']").send_keys("differentPW")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)

# SECOND SET OF ASSERTIONS
print ("Second set of assertions - wrong inputs:")
assert_text_present(driver, "(//div[@class='ng-invalid-touched-feedback ng-star-inserted'])[2]", "Invalid email format", "Test 5 (Invalid Email Format validation)")
assert_text_present(driver, "(//div[@class='ng-invalid-touched-feedback ng-star-inserted'])[3]", "at least 10 characters", "Test 6 (Password minimum length validation)")
assert_text_present(driver, "(//div[@class='invalid-feedback ng-star-inserted'])[1]", "Passwords do not match", "Test 7 (Confirm Password mismatch validation)")


# ----------------------------------------------------------------------------------------------------------------------------------------
# THIRD SET OF ENTRIES - ALREADY USED EMAIL (other 3 fields need to have valid inputs)
clear_and_type(driver, "//input[@aria-label='firstAndLastName']", "test")
clear_and_type(driver, "//input[@aria-label='email']", "test@test.com")
clear_and_type(driver, "//input[@aria-label='password']", "Password321!")
clear_and_type(driver, "//input[@aria-label='confirmPassword']", "Password321!")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)

# THIRD SET OF ASSERTIONS
print ("Third set of assertions - email already in use:")
assert_text_present(driver, "//*[contains(text(),'already exists')]", "An account with that email address already exists.", "Test 8 (Already registered email validation)")


driver.quit()