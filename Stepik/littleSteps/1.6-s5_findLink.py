import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

elem = str(math.ceil(math.pow(math.pi, math.e)*10000))
link = "http://suninjuly.github.io/find_link_text"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    link2 = driver.find_element(By.LINK_TEXT, elem)
    link2.click()

    firstName = driver.find_element(By.NAME, "first_name")
    firstName.send_keys("Maksim")

    secondName = driver.find_element(By.NAME, "last_name")
    secondName.send_keys("Bauer")

    city = driver.find_element(By.CLASS_NAME, "city")
    city.send_keys("South Park")

    country = driver.find_element(By.ID, "country")
    country.send_keys("SoulPlace")

    button = driver.find_element(By.CLASS_NAME, "btn")
    button.click()

    alert=driver.switch_to.alert
    print (alert.text)

finally:
    driver.quit()
    