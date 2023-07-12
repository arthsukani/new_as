import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Selenium WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to the Samsung website
driver.get("https://www.samsung.com")

# Wait for the page to load
wait = WebDriverWait(driver, 20)
driver.implicitly_wait(5)

# Test 1: Click on the "Products" menu item
product = driver.find_element(By.XPATH, "//a[normalize-space()='For Business']")
product.click()

# Test 2: Search for a product
search_input = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class,'search-btn')]/ancestor::li")))
search_input.click()
search_input1 = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='search']")))
search_input1.send_keys("Galaxy S21")
time.sleep(4)
search_input2 = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class,'gnb-search__btn--close')]")))
search_input2.click()

# Test 3:
Insight = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Insights']")))
Insight.click()

# Test 4:
Support = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Support']")))
Support.click()

# Test 5:
Contact_us = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@title='Contact us']")))
Contact_us.click()
time.sleep(2)
driver.quit()
