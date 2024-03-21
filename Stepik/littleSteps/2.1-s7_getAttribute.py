import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/get_attribute.html"


try:
    driver = webdriver.Chrome()
    d = driver.find_element
    driver.get(link)

    x = d(By.ID, "treasure")
    x_val = int(x.get_attribute("valuex"))
    
    def calc(x_val):
        return str(math.log(abs(12*math.sin(x_val))))
    y = calc(x_val)

    answer = d(By.ID, "answer")
    answer.send_keys(y)

    rcbox = d(By.ID, "robotCheckbox")
    rcbox.click()

    rrule = d(By.ID, "robotsRule")
    rrule.click()

    btn = d(By.CSS_SELECTOR, "[type='submit']")
    btn.click()
    
    alert = driver.switch_to.alert
    print (alert.text)
finally:
    driver.quit()
    