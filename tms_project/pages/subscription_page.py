import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from tms_project.pages.base_page import BasePage


class SubscriptionPage(BasePage):
    BRAND_SUBTITLE = (By.CLASS_NAME, 'brand-subtitle')
    PERIOD_1_MONTH = (By.CSS_SELECTOR, '[data-testid="period-1"]')
    PERIOD_3_MONTH = (By.CSS_SELECTOR, '[data-testid="period-3"]')
    PERIOD_12_MONTH = (By.CSS_SELECTOR, '[data-testid="period-12"]')
    PLAN_BASIC = (By.CSS_SELECTOR, '[data-testid="tariff-basic"]')
    PLAN_PREMIUM = (By.CSS_SELECTOR, '[data-testid="tariff-premium"]')
    PLAN_FAMILY = (By.CSS_SELECTOR, '[data-testid="tariff-family"]')
    PROMO_CODE = (By.CSS_SELECTOR, '[data-testid="promo-input"]')
    APPLY_PROMO_CODE = (By.CLASS_NAME, "promo-apply-btn")
    CARD_NUMBER = (By.CSS_SELECTOR, '[data-testid="card-number"]')
    BANK_ELEMENT = (By.CLASS_NAME, 'card-brand')
    EXPIRY_DATE = (By.CSS_SELECTOR, '[data-testid="card-expiry"]')
    CVV = (By.CSS_SELECTOR, '[data-testid="card-cvv"]')
    PROMO_MESSAGE = (By.CSS_SELECTOR, '[data-testid="promo-message"]')

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.url = '/automation-lab/subscription'

        super().__init__(driver, url=self.url, title='Task Management Board')

    @allure.step("Assert that subscription opened")
    def assert_that_subscription_opened(self):
        self.assert_that_page_opened()
        self.assert_element_visible(self.BRAND_SUBTITLE)

    def select_1_month_period(self):
        self.click(self.PERIOD_1_MONTH)

    def select_3_month_period(self):
        self.click(self.PERIOD_3_MONTH)

    def select_12_month_period(self):
        self.click(self.PERIOD_12_MONTH)

    def select_basic_plan(self):
        self.click(self.PLAN_BASIC)

    def select_premium_plan(self):
        self.click(self.PLAN_PREMIUM)

    def select_family_plan(self):
        self.click(self.PLAN_FAMILY)

    def fill_out_the_card(self, card_number, expiry_date, cvv):
        self.send_keys(self.CARD_NUMBER, card_number)
        self.send_keys(self.EXPIRY_DATE, expiry_date)
        self.send_keys(self.CVV, cvv)

    def assert_bank_icon_is_visible(self):
        self.assert_element_visible(self.BANK_ELEMENT)

    def apply_promo_code(self, code):
        self.send_keys(self.PROMO_CODE, code)
        self.click(self.APPLY_PROMO_CODE, is_force=True)

    def get_promo_message_text(self):
        element = self.wait_visible(self.PROMO_MESSAGE)
        return element.text
