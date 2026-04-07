import allure
from tms_project.pages.login_page import LoginPage
from tms_project.pages.dashboard_page import DashboardPage
from tms_project.components.dashboard_modal_component import CreateBoardModalComponent
from tms_project.test_data.users import BOB


@allure.feature("Dashboard")
@allure.title("Displaying page and information about tasks and boards")
def test_dashboard_display_and_info(driver):

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(BOB)

    dashboard_page = DashboardPage(driver)
    with allure.step("Assert that dashboard page is displayed"):
        dashboard_page.assert_that_dashboard_opened()
        dashboard_page.assert_dashboard_display_and_info_visible()


@allure.feature("Dashboard")
@allure.title("Creating new dashboard")
def test_create_new_board(driver):
    with allure.step("User is logged in"):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(BOB)

        with allure.step("Wait for dashboard to load"):
            dashboard_page = DashboardPage(driver)
            dashboard_page.assert_that_dashboard_opened()

    with allure.step("Open modal, fill and save new board"):
        dashboard_page.open_create_board_modal()
        modal = CreateBoardModalComponent(driver)

        modal.set_title("NEW DASHBOARD")
        modal.set_description("DESCRIPTION")
        modal.make_public()
        modal.save()

    dashboard_page.assert_that_dashboard_was_created()
