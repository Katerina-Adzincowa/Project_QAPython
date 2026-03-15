import allure
import pytest
from tms_project.pages.dashboard_page import DashboardPage
from tms_project.pages.login_page import LoginPage
from tms_project.test_data.users import BOB


@pytest.mark.smoke
@allure.title("Login")
def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(BOB)

    dashboard_page = DashboardPage(driver)
    dashboard_page.assert_that_dashboard_opened()
    with allure.step("Assert that the user was logged in"):
        dashboard_page.assert_that_user_name_is_the_same_user(BOB.name)
