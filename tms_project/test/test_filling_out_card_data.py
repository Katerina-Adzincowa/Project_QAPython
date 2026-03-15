import allure
import pytest
from tms_project.pages.subscription_page import SubscriptionPage

CARD_NUMBER = "5555 5555 5555 4444"
EXPIRY_DATE = "062026"
CVV = "322"


@allure.title("Card filling out")
@pytest.mark.smoke
def test_fill_out_the_card(driver):
    subscription_page = SubscriptionPage(driver)
    subscription_page.open()
    subscription_page.assert_that_subscription_opened()
    subscription_page.fill_out_the_card(CARD_NUMBER, EXPIRY_DATE, CVV)
    with allure.step("Bank icon is visible"):
        subscription_page.assert_bank_icon_is_visible()
