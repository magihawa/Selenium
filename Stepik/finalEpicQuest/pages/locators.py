from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group>a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    CHECKOUT_BTN = (By.CSS_SELECTOR, ".col-sm-4 > .btn")
    EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner>p")


class LoginPageLocators():
    IN_URL_ASSERT = "login"
    LOGIN_USERNAME = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")

    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD_REPEAT = (
        By.ID, "id_registration-password2")


class StorePageLocators():
    ADD_TO_BASKET_BTN = (By.CLASS_NAME, "btn-add-to-basket")

    NAME = (By.CSS_SELECTOR, ".product_main > h1")
    ALERT_WITH_NAME = (
        By.CSS_SELECTOR, ".alert-success > .alertinner > strong")

    PRICE = (By.CSS_SELECTOR, ".product_main > p.price_color")
    ALERT_WITH_PRICE = (By.CSS_SELECTOR, ".alert-info > .alertinner > p")
