
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Define Variables
URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
pause = 5

# Navigate to the login page of Sauce Demo
driver.get(URL)
time.sleep(pause)

# Define Elements as Variables
Username = driver.find_element(By.ID,"user-name")
Password = driver.find_element(By.ID,"password")
Login = driver.find_element(By.ID,"login-button")

# Perform Login
Username.send_keys(USERNAME)
time.sleep(pause)

Password.send_keys(PASSWORD)
time.sleep(pause)

Login.click()
time.sleep(pause)

# Define Menu and Logout buttons
menu = driver.find_element(By.ID,"react-burger-menu-btn")
Logout = driver.find_element(By.ID,"logout_sidebar_link")

# List of products to add to cart
PRODUCT = [
    "add-to-cart-sauce-labs-backpack",
    "add-to-cart-sauce-labs-bike-light",
    "add-to-cart-sauce-labs-bolt-t-shirt",
    "add-to-cart-sauce-labs-fleece-jacket",
    "add-to-cart-sauce-labs-onesie",
    "add-to-cart-test.allthethings()-t-shirt-(red)"
]

# Add product to cart using a loop
for product_id in PRODUCT:
    driver.find_element(By.ID, product_id).click()
time.sleep(pause)

# Click burger menu
menu.click()
time.sleep(pause)

# Click on Logout
Logout.click()
time.sleep(pause)