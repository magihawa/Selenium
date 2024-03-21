import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    x = driver.find_element(By.ID, "num1")
    x_val = x.text
    y = driver.find_element(By.ID, "num2")
    y_val = y.text

    def add(x_val, y_val):
        return int(x_val)+int(y_val)
    z = str(add(x_val, y_val))

    select = Select(driver.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(z)

    btn = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
    btn.click()
    
    alert = driver.switch_to.alert
    print (alert.text)
finally:
    driver.quit()
    