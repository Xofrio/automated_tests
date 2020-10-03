from .pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('offer_number', ["0", "1", "2", "3", "4", "5", "6",
                                          pytest.param("7", marks=pytest.mark.xfail(reason="unknown bug")),
                                          "8", "9"])
def test_should_be_add_to_cart_button(browser, offer_number):
    browser.delete_all_cookies()
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_number}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.check_basket_product()
    product_page.check_basket_value()
