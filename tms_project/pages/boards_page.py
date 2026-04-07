import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from tms_project.pages.base_page import BasePage


class BoardPage(BasePage):
    CREATE_BOARD_BUTTON = (By.CSS_SELECTOR, '[data-qa="boards-create-board-button"]')
    TABLE = (By.CLASS_NAME, 'admin-table')
    TITLE = (By.CSS_SELECTOR, '[data-qa="boards-page-title"]')
    EMPTY_BOARDS_MESSAGE = (By.XPATH, "//td[contains(text(), 'Доски не найдены')]")
    USER_INFO = (By.CSS_SELECTOR, '[data-qa="header-user-info"]')
    ANY_OPEN_LINK = (By.XPATH, "//a[text()='Открыть']")
    ANY_BOARD_TOGGLE = (By.CSS_SELECTOR, '[data-qa^="toggle-board-tasks-"]')

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.url = '/boards'
        super().__init__(driver, self.url)

    @allure.step("Open board with ID: {board_id}")
    def open_specific_board(self, board_id: str):
        locator = (By.CSS_SELECTOR, f'a[href="/boards/{board_id}"]')
        self.click(locator)

    @allure.step("Read the info with toggle")
    def open_board_description(self, board_id: str):
        locator = (By.CSS_SELECTOR, f'[data-qa="toggle-board-tasks-{board_id}"]')
        self.click(locator)

    @allure.step("Assert that board page opened")
    def assert_that_boards_page_opened(self):
        self.assert_that_page_opened()
        self.assert_element_visible(self.CREATE_BOARD_BUTTON)
        self.assert_element_visible(self.USER_INFO)
        self.assert_element_visible(self.TITLE)

    @allure.step("Assert that table is not empty)")
    def assert_boards_are_present(self):
        self.assert_element_visible(self.TABLE)
        self.assert_element_visible(self.ANY_OPEN_LINK)
        self.assert_element_visible(self.ANY_BOARD_TOGGLE)

    @allure.step("Assert that board is empty")
    def assert_no_boards_present(self):
        self.assert_element_visible(self.EMPTY_BOARDS_MESSAGE)
        self.assert_text_contain_in_element(self.EMPTY_BOARDS_MESSAGE, "Доски не найдены")
