import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"

try:
    driver.get(link)

    x = driver.find_element(By.ID, "input_value")
    x_val = int(x.text)

    def calc(x_val):
        return str(math.log(abs(12*math.sin(x_val))))
    y = calc(x_val)

    answer = driver.find_element(By.ID, "answer")
    answer.send_keys(y)

    driver.execute_script("window.scrollBy(0,100);")

    rcheck = driver.find_element(By.ID, "robotCheckbox")
    rcheck.click()

    rrule = driver.find_element(By.ID, "robotsRule")
    rrule.click()

    button = driver.find_element(By.TAG_NAME, "button")
    button.click()

    alert = driver.switch_to.alert
    alert_txt = alert.text
    al = alert_txt.split(': ')[-1]
    print (al)
finally:
    driver.quit







# try:
#     browser = webdriver.Chrome()
#     browser.execute_script("document.title='Script executing';alert('Robots at work');")
#     time.sleep(10)
    
# finally:
#     browser.quit
