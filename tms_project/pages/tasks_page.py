import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from tms_project.pages.base_page import BasePage


class TaskPage(BasePage):
    TITLE = (By.CSS_SELECTOR, '[data-qa="tasks-page-title"]')
    TABLE = (By.CLASS_NAME, 'admin-table')
    STATUS_FILTER = (By.CSS_SELECTOR, '[data-qa="tasks-status-filter"]')
    PRIORITY_FILTER = (By.CSS_SELECTOR, '[data-qa="tasks-priority-filter"]')
    ANY_OPEN_LINK = (By.XPATH, "//a[text()='Открыть']")
    SEARCH_FIELD = (By.CSS_SELECTOR, '[data-qa="tasks-search-input"]')
    USER_INFO = (By.CSS_SELECTOR, '[data-qa="header-user-info"]')
    FIRST_PAGINATION_PAGE = (By.CSS_SELECTOR, '[data-qa="pagination-page-1"]')

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.url = '/tasks'
        super().__init__(driver, self.url)

    @allure.step("Assert that tasks page opened")
    def assert_that_tasks_page_opened(self):
        self.assert_that_page_opened()
        self.assert_element_visible(self.TITLE)
        self.assert_text_contain_in_element(self.TITLE, "Все задачи")
        self.assert_element_visible(self.USER_INFO)
        self.assert_element_visible(self.SEARCH_FIELD)
        self.assert_element_visible(self.STATUS_FILTER)
        self.assert_element_visible(self.PRIORITY_FILTER)

    @allure.step("Assert that tasks are present in the table")
    def assert_tasks_are_present(self):
        self.assert_element_visible(self.TABLE)
        self.assert_element_visible(self.ANY_OPEN_LINK)
        self.assert_element_visible(self.FIRST_PAGINATION_PAGE)

    @allure.step("Get the number of tasks displayed on the page")
    def get_tasks_count(self) -> int:
        elements = self.driver.find_elements(*self.ANY_OPEN_LINK)
        return len(elements)

