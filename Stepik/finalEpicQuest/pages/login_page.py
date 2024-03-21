from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert LoginPageLocators.IN_URL_ASSERT in current_url, f"Expected {LoginPageLocators.IN_URL_ASSERT} in URL, but got: {
            current_url} without expected string"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_USERNAME), "Login username form is not found"
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_PASSWORD), "Login password form is not found"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_EMAIL), "Registration email form is not found"
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_PASSWORD), "Registration password form is not found"
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_PASSWORD_REPEAT), "Registration password repeat form is not found"

    def register_new_user(self, email, password):
        self.browser.find_element(
            *LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(
            *LoginPageLocators.REGISTRATION_PASSWORD).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.REGISTRATION_PASSWORD_REPEAT).send_keys(password)
        register_btn = self.browser.find_element(
            By.NAME, "registration_submit")
        register_btn.click()
