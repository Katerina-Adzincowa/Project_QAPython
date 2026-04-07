import allure
import pytest
from tms_project.pages.login_page import LoginPage
from tms_project.pages.tasks_page import TaskPage
from tms_project.pages.dashboard_page import DashboardPage
from tms_project.test_data.users import BOB
from tms_project.test_data.users import NEWBOB


@allure.feature("Tasks")
@allure.title("Display of tasks page and table (User with tasks)")
def test_tasks_presence(driver):
    with allure.step("User is logged in"):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(BOB)

    with allure.step("Wait for Dashboard to load after login"):
        dashboard_page = DashboardPage(driver)
        dashboard_page.assert_that_dashboard_opened()

    with allure.step("Assert that tasks page and table are displayed"):
        task_page = TaskPage(driver)
        task_page.open()

        task_page.assert_that_tasks_page_opened()
        task_page.assert_tasks_are_present()


@allure.feature("Tasks")
@allure.title("Display of empty tasks page (User without tasks)")
@pytest.mark.xfail(reason="BUG: New user sees tasks from other users. Expected count: 0")
def test_tasks_absence(driver):
    with allure.step("User with no tasks is logged in"):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(NEWBOB)

    with allure.step("Wait for Dashboard to load after login"):
        dashboard_page = DashboardPage(driver)
        dashboard_page.assert_that_dashboard_opened()

    with allure.step("Assert that tasks list is empty"):
        task_page = TaskPage(driver)
        task_page.open()
        task_page.assert_that_tasks_page_opened()
        count = task_page.get_tasks_count()

        assert count == 0, f"Expected 0 tasks for new user, but found {count}!"
