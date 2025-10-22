from selenium import webdriver
from selenium.webdriver.common.by import By


def login():

    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    usuario = driver.find_element(By.ID, "user-name").send_keys("standard_user")
    password = driver.find_element(By.ID, "password").send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()

    print(driver.find_element(By.CLASS_NAME, "login-logo"))

    time.sleep(2)
