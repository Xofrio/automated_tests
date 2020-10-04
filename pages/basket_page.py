from .base_page import BasePage
from .locators import BasketPageLocators
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
            "Basket is not empty!"

    def should_be_message_about_emptiness(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), \
            "Basket doesn't have a message about emptiness"
