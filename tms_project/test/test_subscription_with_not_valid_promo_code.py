import allure
import pytest

from tms_project.pages.subscription_page import SubscriptionPage
from tms_project.test_data.promo_codes import INVALID_PROMO_EXPIRED, EXPECTED_ERROR_MSG_EXP


@allure.title("Not valid promo code")
@pytest.mark.smoke
def test_not_valid_promo_code(driver):
    subscription_page = SubscriptionPage(driver)
    subscription_page.open()
    subscription_page.assert_that_subscription_opened()
    subscription_page.select_3_month_period()
    subscription_page.select_family_plan()
    subscription_page.apply_promo_code(INVALID_PROMO_EXPIRED)
    actual_text = subscription_page.get_promo_message_text()
    with allure.step("Assert that error message exists"):
        assert EXPECTED_ERROR_MSG_EXP in actual_text
