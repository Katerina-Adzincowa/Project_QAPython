import allure
from tms_project.pages.login_page import LoginPage
from tms_project.pages.boards_page import BoardPage
from tms_project.pages.dashboard_page import DashboardPage
from tms_project.test_data.users import BOB
from tms_project.test_data.users import NEWBOB


@allure.feature("Boards")
@allure.title("Display of boards page and table")
def test_boards_presence(driver):
    with allure.step("User is logged in"):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(BOB)

    with allure.step("Wait for dashboard to load"):
        dashboard_page = DashboardPage(driver)
        dashboard_page.assert_that_dashboard_opened()

    with allure.step("Assert that board page is displayed"):
        board_page = BoardPage(driver)
        board_page.open()

        board_page.assert_that_boards_page_opened()
        board_page.assert_boards_are_present()


@allure.feature("Boards")
@allure.title("Display of boards page and table")
def test_boards_absence(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(NEWBOB)

    with allure.step("Dashboard page after login with user with no boards created"):
        dashboard_page = DashboardPage(driver)
        dashboard_page.assert_that_dashboard_opened()

    with allure.step("Assert that board page is empty"):
        board_page = BoardPage(driver)
        board_page.open()

        board_page.assert_that_boards_page_opened()
        board_page.assert_no_boards_present()
