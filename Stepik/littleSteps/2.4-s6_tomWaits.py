import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    driver.get(link)

    price = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    btn = driver.find_element(By.ID, "book")
    btn.click()

    x = driver.find_element(By.ID, "input_value")
    x_val = int(x.text)

    def calc(x_val):
        return str(math.log(abs(12*math.sin(x_val))))
    y = calc(x_val)

    answer=driver.find_element(By.ID, "answer")
    answer.send_keys(y)

    btn2 = driver.find_element(By.ID, "solve")
    btn2.click()

    print (driver.switch_to.alert.text)
finally:
    driver.quit
