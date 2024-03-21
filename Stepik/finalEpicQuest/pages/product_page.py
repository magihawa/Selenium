from .base_page import BasePage
from .locators import StorePageLocators


class ProductPage(BasePage):

    def should_be_present(self):
        assert self.is_element_present(
            *StorePageLocators.ALERT_WITH_NAME), "SUCCESS MESSAGE is not present"

    def should_not_be_present(self):
        assert self.is_not_element_present(
            *StorePageLocators.ALERT_WITH_NAME), "SUCCESS MESSAGE is present, but should not be"

    def should_disappear(self):
        assert self.is_disappeared(
            *StorePageLocators.ALERT_WITH_NAME), "SUCCESS MESSAGE has not disappear"

    def add_to_basket(self):
        btn = self.browser.find_element(*StorePageLocators.ADD_TO_BASKET_BTN)
        btn.click()

    def should_be_equal_price_in_notification(self):
        expected_price = self.browser.find_element(
            *StorePageLocators.PRICE).text
        notification_price = self.browser.find_element(
            *StorePageLocators.ALERT_WITH_PRICE).text
        assert expected_price in notification_price, f"Expected {
            expected_price}, but got: {notification_price}"
        print(f"{expected_price}, ------ {notification_price}")

    def should_be_equal_name_in_notification(self):
        expected_name = self.browser.find_element(*StorePageLocators.NAME).text
        notification_name = self.browser.find_element(
            *StorePageLocators.ALERT_WITH_NAME).text
        assert expected_name == notification_name, f"Expected {
            expected_name}, but got: {notification_name}"
        print(f"{expected_name}, ------ {notification_name}")
