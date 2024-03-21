import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_data(link):
    driver = webdriver.Chrome()
    driver.get(link)
    firstName = driver.find_element(By.CLASS_NAME, "first").send_keys("Maksim")
    secondName = driver.find_element(
        By.CSS_SELECTOR, "[placeholder*=last]").send_keys("Bauer")
    email = driver.find_element(
        By.CLASS_NAME, "third").send_keys("mbauer@pochta.com")
    button = driver.find_element(By.XPATH, "//*[@type='submit']").click()
    time.sleep(1)
    return driver.find_element(By.TAG_NAME, "h1").text


class TestWelcome(unittest.TestCase):
    def test_reg1(self):
        self.assertEqual(test_data("http://suninjuly.github.io/registration1.html"),
                         "Congratulations! You have successfully registered!", "1st page registration")

    def test_reg2(self):
        self.assertEqual(test_data("http://suninjuly.github.io/registration2.html"),
                         "Congratulations! You have successfully registered!", "2nd page registration")


if __name__ == "__main__":
    unittest.main()
