from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
            "Basket is not empty!"

    def should_be_message_about_emptiness(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), \
            "Basket doesn't have a message about emptiness"
