import allure
import pytest

from tms_project.pages.dashboard_page import DashboardPage
from tms_project.pages.registration_page import RegistrationPage
from tms_project.test_data.users import NEWBOB


@pytest.mark.tms
@allure.title("User registration")
@pytest.mark.smoke
def test_register_new_user(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    registration_page.register(NEWBOB)

    dashboard_page = DashboardPage(driver)
    with allure.step("Assert that new user has been registered"):
        dashboard_page.assert_that_dashboard_opened()
        dashboard_page.assert_that_user_name_is_the_same_user(NEWBOB.name)
