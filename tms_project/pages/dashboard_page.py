import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tms_project.pages.base_page import BasePage


class DashboardPage(BasePage):
    CREATE_BOARD_BUTTON = (By.CSS_SELECTOR, '[data-qa="dashboard-create-board-button"]')
    DASHBOARD_STATISTIC = (By.CSS_SELECTOR, '[data-qa="dashboard-stats"]')
    PANEL_ALL_BOARDS = (By.CSS_SELECTOR, '[data-qa="sidebar-boards-link"]')
    PANEL_ALL_TASKS = (By.CSS_SELECTOR, '[data-qa="sidebar-tasks-link"]')
    USER_INFO = (By.CSS_SELECTOR, '[data-qa="header-user-info"]')
    MODAL_WINDOW = (By.CSS_SELECTOR, '[data-qa="create-board-modal"]')
    TOAST_MESSAGE = (By.CLASS_NAME, "toast-message")

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.url = '/dashboard'
        super().__init__(driver, self.url)

    @allure.step("Assert that dashboard opened")
    def assert_that_dashboard_opened(self):
        self.assert_that_page_opened()
        self.assert_element_visible(self.CREATE_BOARD_BUTTON)
        self.assert_element_visible(self.USER_INFO)

    @allure.step("Assert that dashboard information and panels are visible")
    def assert_dashboard_display_and_info_visible(self):
        self.assert_element_visible(self.DASHBOARD_STATISTIC)
        self.assert_element_visible(self.PANEL_ALL_BOARDS)
        self.assert_element_visible(self.PANEL_ALL_TASKS)

    @allure.step("Click on 'Create Board' button to open the modal")
    def open_create_board_modal(self):
        self.click(self.CREATE_BOARD_BUTTON)

    @allure.step("Assert that board was successfully created (Toast message)")
    def assert_that_dashboard_was_created(self):
        toast_element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.TOAST_MESSAGE)
        )

        message_text = toast_element.text
        assert message_text == "Доска успешно создана!"
