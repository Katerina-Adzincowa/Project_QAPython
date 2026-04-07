import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from tms_project.pages.base_page import BasePage


class AdminPage(BasePage):
    TITLE = (By.CLASS_NAME, 'admin-section-title')
    SEARCH_INPUT = (By.CSS_SELECTOR, '[data-qa="input"]')
    USER_NAME = (By.CSS_SELECTOR, '[data-qa="header-username"]')
    ADMIN_PANEL = (By.CSS_SELECTOR, '[data-qa="sidebar-admin-link"]')
    TABLE = (By.CLASS_NAME, 'admin-table-container')

    EDIT_ROLE_SELECT = (By.CSS_SELECTOR, '[data-qa="edit-user-role-select"]')
    SAVE_USER_BUTTON = (By.CSS_SELECTOR, '[data-qa="edit-user-save-button"]')

    ERROR_TOAST = (By.XPATH, "//*[contains(text(), 'Доступ запрещён (403)')]")

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.url = '/admin'
        super().__init__(driver, self.url)

    @allure.step("Edit user with ID: {user_id}")
    def edit_user_by_id(self, user_id: str):
        locator = (By.CSS_SELECTOR, f'[data-qa="edit-user-button-{user_id}"]')
        self.click(locator)

    @allure.step("Select new role: {role_name}")
    def change_user_role(self, role_name: str):
        select_element = self.wait_visible(self.EDIT_ROLE_SELECT)
        dropdown = Select(select_element)
        dropdown.select_by_visible_text(role_name)

    @allure.step("Save user edits")
    def save_user_edits(self):
        self.click(self.SAVE_USER_BUTTON)

    @allure.step("Delete user with ID: {user_id}")
    def delete_user_by_id(self, user_id: str):
        locator = (By.CSS_SELECTOR, f'[data-qa="delete-user-button-{user_id}"]')
        self.click(locator)

    @allure.step("Search for user by text: {search_text}")
    def search_user(self, search_text: str):
        search_field = self.wait_visible(self.SEARCH_INPUT)
        search_field.clear()
        search_field.send_keys(search_text)

    @allure.step("Assert that Admin page opened successfully")
    def assert_that_admin_page_opened(self):
        self.assert_that_page_opened()
        self.assert_element_visible(self.TITLE)
        self.assert_element_visible(self.TABLE)
        self.assert_element_visible(self.SEARCH_INPUT)
        self.assert_text_contain_in_element(self.USER_NAME, "admin")
        self.assert_text_contain_in_element(self.ADMIN_PANEL, "Административная панель")

    @allure.step("Assert that user '{expected_user}' is visible in the table")
    def assert_user_in_table(self, expected_user: str):
        self.assert_text_contain_in_element(self.TABLE, expected_user)

    @allure.step("Assert that access denied toast (403) is visible")
    def assert_access_denied_toast(self):
        self.assert_element_visible(self.ERROR_TOAST)
