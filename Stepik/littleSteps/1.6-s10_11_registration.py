import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    firstName = driver.find_element(By.CLASS_NAME, "first")
    firstName.send_keys("Maksim")

    secondName = driver.find_element(By.CSS_SELECTOR, "[placeholder*=last]")
    secondName.send_keys("Bauer")

    email = driver.find_element(By.CLASS_NAME, "third")
    email.send_keys("mbauer@pochta.com")

    button = driver.find_element(By.XPATH, "//*[@type='submit']")
    button.click()

    time.sleep(1)

    success = driver.find_element(By.TAG_NAME, "h1")
    welcome_text = success.text
    assert "Congratulations! You have successfully registered!" == welcome_text
    
finally:
    time.sleep(3)
    driver.quit()
    