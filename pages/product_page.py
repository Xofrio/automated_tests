from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), \
            "There should be add to cart button!"
        button = self.is_element_present(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def check_basket_product(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGES), \
            "There should be messages after pressing button!"
        product_name = self.is_element_present(*ProductPageLocators.PRODUCT_NAME).text
        basket_product = self.is_element_present(*ProductPageLocators.BASKET_PRODUCT).text
        assert basket_product in product_name, f"Expected {product_name} to be in message about basket product," \
                                               f" got {basket_product}"

    def check_basket_value(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGES), \
            "There should be messages after pressing button!"
        product_price = self.is_element_present(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.is_element_present(*ProductPageLocators.BASKET_PRICE).text
        assert basket_price in product_price, f"Expected {product_price} to be in message about basket value," \
                                              f" got {basket_price}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should disappear, but it did not"
