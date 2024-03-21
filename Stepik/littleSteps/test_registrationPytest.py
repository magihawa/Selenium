import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()


def test_data(link):
    driver.get(link)
    firstName = driver.find_element(By.CLASS_NAME, "first").send_keys("Maksim")
    secondName = driver.find_element(
        By.CSS_SELECTOR, "[placeholder*=last]").send_keys("Bauer")
    email = driver.find_element(
        By.CLASS_NAME, "third").send_keys("mbauer@pochta.com")
    button = driver.find_element(By.XPATH, "//*[@type='submit']").click()
    time.sleep(1)
    return driver.find_element(By.TAG_NAME, "h1").text


class TestWelcome():
    def test_reg1(self):
        try:
            assert test_data(
                "http://suninjuly.github.io/registration1.html") == "Congratulations! You have successfully registered!", "1st page registration"
        finally:
            driver.quit()

    def test_reg2(self):
        try:
            assert test_data(
                "http://suninjuly.github.io/registration2.html") == "Congratulations! You have successfully registered!", "2nd page registration"
            # with pytest.raises(NoSuchElementException):
            #     driver.find_element(By.CSS_SELECTOR, "[placeholder*=last]")
            #     pytest.fail("Не должно быть кнопки LastName")
        finally:
            driver.quit()
