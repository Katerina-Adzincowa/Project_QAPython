import allure
import pytest

from tms_project.pages.subscription_page import SubscriptionPage
from tms_project.test_data.promo_codes import VALID_PROMO, EXPECTED_SUCCESS_MSG


@allure.title("Valid promo code")
@pytest.mark.smoke
def test_apply_valid_promo_code_for_premium_plan(driver):
    subscription_page = SubscriptionPage(driver)
    subscription_page.open()
    subscription_page.assert_that_subscription_opened()
    subscription_page.select_12_month_period()
    subscription_page.select_premium_plan()
    subscription_page.apply_promo_code(VALID_PROMO)
    actual_text = subscription_page.get_promo_message_text()
    with allure.step("Assert that promo code was applied"):
        assert EXPECTED_SUCCESS_MSG in actual_text
