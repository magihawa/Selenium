import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"

try:
    driver.get(link)
    fname = driver.find_element(By.NAME, "firstname")
    fname.send_keys("Maksim")
    lname = driver.find_element(By.NAME, "lastname")
    lname.send_keys("Bauer")
    email = driver.find_element(By.NAME, "email")
    email.send_keys("mbauer@pochta.ru")

    file = driver.find_element(By.NAME, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_txt = os.path.join(current_dir, 'file.txt')
    file.send_keys(file_txt)

    btn = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
    btn.click()
    
    alert = driver.switch_to.alert
    print(alert.text)

finally:
    driver.quit

# try:
#     browser = webdriver.Chrome()
#     browser.execute_script("document.title='Script executing';alert('Robots at work');")
#     time.sleep(10)
    
# finally:
#     browser.quit
# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
# print (current_dir + "???????????????????????????")
# file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
# print (file_path + "???????????????????????????")