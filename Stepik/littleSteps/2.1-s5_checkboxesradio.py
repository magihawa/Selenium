import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/math.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    x = driver.find_element(By.ID, "input_value")
    x_val = x.text

    def calc(x_val):
        return str(math.log(abs(12*math.sin(int(x_val)))))
    y = calc(x_val)

    answer = driver.find_element(By.ID, "answer")
    answer.send_keys(y)

    rcbox = driver.find_element(By.ID, "robotCheckbox")
    rcbox.click()

    rrule = driver.find_element(By.ID, "robotsRule")
    rrule.click()

    btn = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
    btn.click()
    
    alert = driver.switch_to.alert
    print (alert.text)
finally:
    time.sleep(3)
    driver.quit()
    