from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.is_element_present(*LoginPageLocators.GUEST_EMAIL).send_keys(email)
        self.is_element_present(*LoginPageLocators.GUEST_PASSWORD).send_keys(password)
        self.is_element_present(*LoginPageLocators.GUEST_REPEAT_PASSWORD).send_keys(password)
        self.is_element_present(*LoginPageLocators.REGISTER_BUTTON).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Not a login page, there should be " \
                                                        "/login/ at the end of the link."

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "No login form present."

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "No register form present."
