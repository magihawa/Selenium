from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_present(self):
        assert self.is_not_element_present(
            *BasketPageLocators.CHECKOUT_BTN), "Checkout button is present, but should not be"

    def should_be_present(self):
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_TEXT), "The basket is not empty"
