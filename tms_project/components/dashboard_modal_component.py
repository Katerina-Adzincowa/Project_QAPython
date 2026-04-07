import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from tms_project.pages.base_page import BasePage


class CreateBoardModalComponent(BasePage):
    def __init__(self, driver):
        super().__init__(driver, url=None)
        self.driver: WebDriver = driver

        self.component = f'[data-qa="create-board-modal"]'
        self.COMPONENT = (By.CSS_SELECTOR, f"{self.component}")

        self.CLOSE_BUTTON = (By.CSS_SELECTOR, f'{self.component} [data-qa="modal-close-button"]')
        self.TITLE_INPUT = (By.CSS_SELECTOR, f'{self.component} [data-qa="create-board-title-input"]')

        self.DESCRIPTION_TEXT = (By.CSS_SELECTOR, f'{self.component} [data-qa="create-board-description-textarea"]')
        self.MAKE_PUBLIC = (By.CSS_SELECTOR, f'{self.component} [data-qa="create-board-public-checkbox"]')

        self.CANCEL_BUTTON = (By.CSS_SELECTOR, f'{self.component} [data-qa="create-board-cancel-button"]')
        self.SUBMIT_BUTTON = (By.CSS_SELECTOR, f'{self.component} [data-qa="create-board-submit-button"]')

    @allure.step("Close the modal window")
    def close_modal(self):
        self.click(self.CLOSE_BUTTON)

    @allure.step("Make public")
    def make_public(self):
        self.click(self.MAKE_PUBLIC)

    @allure.step("Click the 'Submit' button")
    def save(self):
        self.click(self.SUBMIT_BUTTON)

    @allure.step("Enter the board name: {title}")
    def set_title(self, title):
        self.send_keys(self.TITLE_INPUT, title)

    @allure.step("Enter board description")
    def set_description(self, text: str):
        self.send_keys(self.DESCRIPTION_TEXT, text)
