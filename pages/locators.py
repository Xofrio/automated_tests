from selenium.webdriver.common.by import By


class ProductPageLocators():
    ADD_TO_BASKET = (By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
    MESSAGES = (By.XPATH, "//*[@id='messages']/div")
    PRODUCT_NAME = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    BASKET_PRODUCT = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    BASKET_PRICE = (By.XPATH, "//*[@id='messages']/div[3]/div/p/strong")