import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLoginAndSubmit:
    @pytest.mark.parametrize("num", ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
    def test_login_submit(self, browser, num):
        link = f"https://stepik.org/lesson/{num}/step/1"
        browser.get(link)
        self.login(browser)
        self.submit_answer(browser)

    def login(self, browser):
        login_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "navbar__auth_login"))
        )
        login_btn.click()

        email_input = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "id_login_email"))
        )
        email_input.send_keys("PUT Ur LOGIN HErE")

        password_input = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "id_login_password"))
        )
        password_input.send_keys("PUT Ur PASSWOrD HErE")

        login_btn2 = browser.find_element(By.CLASS_NAME, "sign-form__btn")
        login_btn2.click()
        # time.sleep(3)

    def submit_answer(self, browser):
        textarea = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "ember-text-area"))
        )
        textarea.send_keys(str(math.log(int(time.time()))))

        submit_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
        )
        submit_btn.click()

        feedback_element = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "smart-hints__hint"))
        )
        feedback_text = feedback_element.text

        if feedback_text != "Correct!":
            print("Test failed: Incorrect feedback received:", feedback_text)
        else:
            print("Test passed: Correct feedback received.")

        assert feedback_text == "Correct!", f"Expected feedback: 'Correct!', but got: '{
            feedback_text}'"


if __name__ == "__main__":
    pytest.main(['-s', '-v'])
