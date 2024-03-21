import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"

try:
    driver.get(link)
    btn = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
    btn.click()

    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(1)

    x=driver.find_element(By.ID, "input_value")
    x_val = int(x.text)

    def calc(x_val):
        return str(math.log(abs(12*math.sin(x_val))))
    y = calc(x_val)

    answer=driver.find_element(By.ID, "answer")
    answer.send_keys(y)

    btn2 = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
    btn2.click()

    print(driver.switch_to.alert.text)
finally:
    driver.quit
