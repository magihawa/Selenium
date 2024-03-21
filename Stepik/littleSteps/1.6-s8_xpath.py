import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_xpath_form"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    firstName = driver.find_element(By.NAME, "first_name")
    firstName.send_keys("Maksim")

    secondName = driver.find_element(By.NAME, "last_name")
    secondName.send_keys("Bauer")

    city = driver.find_element(By.CLASS_NAME, "city")
    city.send_keys("South Park")

    country = driver.find_element(By.ID, "country")
    country.send_keys("SoulPlace")

    button = driver.find_element(By.XPATH, "//*[@type='submit']")
    button.click()

    alert=driver.switch_to.alert
    print (alert.text)

finally:
    driver.quit()
    