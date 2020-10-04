from selenium.webdriver.common.by import By


class BasePageLocators():
    BASKET_LINK = (By.XPATH, "//a[@class='btn btn-default']")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_EMPTY = (By.XPATH, "//*[@id='content_inner']/p")
    BASKET_ITEM = (By.XPATH, "//div[@class='basket-items']")


class LoginPageLocators():
    GUEST_EMAIL = (By.XPATH, "//input[@name='registration-email']")
    GUEST_PASSWORD = (By.XPATH, "//input[@name='registration-password1']")
    GUEST_REPEAT_PASSWORD = (By.XPATH, "//input[@name='registration-password2']")
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")
    REGISTER_BUTTON = (By.XPATH, "//button[@name='registration_submit']")
    REGISTER_FORM = (By.XPATH, "//form[@id='register_form']")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators():
    ADD_TO_BASKET = (By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
    BASKET_PRICE = (By.XPATH, "//*[@id='messages']/div[3]/div/p/strong")
    BASKET_PRODUCT = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    MESSAGES = (By.XPATH, "//*[@id='messages']/div")
    PRODUCT_NAME = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div")
