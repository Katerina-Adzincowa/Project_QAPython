import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from tms_project.pages.base_page import BasePage
from tms_project.test_data.users import User


class RegistrationPage(BasePage):

    USERNAME_INPUT = (By.ID, 'id-input-register-username-input')
    EMAIL_INPUT = (By.ID, 'id-input-register-email-input')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[data-qa="register-password-input"]')
    PASSWORD_CONFIRMATION_INPUT = (By. CSS_SELECTOR, '[id="id-input-register-confirm-password-input"]')
    SUBMIT_REGISTRATION = (By. CSS_SELECTOR, '[data-qa="register-submit-button"]')

    def __init__(self, driver):
        self.url = '/register'

        super().__init__(driver, self.url)
        self.driver: WebDriver = driver

    @allure.step("Registration with creds {user}")
    def register(self, user: User):
        self.send_keys(self.USERNAME_INPUT, user.name)
        self.send_keys(self.EMAIL_INPUT, user.email)
        self.send_keys(self.PASSWORD_INPUT, user.password)
        self.send_keys(self.PASSWORD_CONFIRMATION_INPUT, user.password_confirmation)
        self.click(self.SUBMIT_REGISTRATION)
