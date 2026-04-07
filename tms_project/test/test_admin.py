import allure
from tms_project.pages.login_page import LoginPage
from tms_project.pages.admin_page import AdminPage
from tms_project.pages.dashboard_page import DashboardPage
from tms_project.test_data.users import ADMIN, BOB


@allure.feature("Admin panel")
@allure.title("Admin can access the Admin page")
def test_admin_access_allowed(driver):
    with allure.step("Admin is logged in"):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(ADMIN)

        dashboard_page = DashboardPage(driver)
        dashboard_page.assert_that_dashboard_opened()

    with allure.step("Admin opens Admin page"):
        admin_page = AdminPage(driver)
        admin_page.open()
        admin_page.assert_that_admin_page_opened()


@allure.title("Admin can search for a user in the table")
def test_admin_search_user(driver):
    with allure.step("Admin is logged in and opens Admin page"):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(ADMIN)
        dashboard_page = DashboardPage(driver)
        dashboard_page.assert_that_dashboard_opened()

        admin_page = AdminPage(driver)
        admin_page.open()
        admin_page.assert_that_admin_page_opened()

    with allure.step("Search for user 'bob_user'"):
        search_text = "bob_user"
        admin_page.search_user(search_text)

    with allure.step("Assert search results contain the requested user"):
        admin_page.assert_user_in_table(search_text)


@allure.title("Non-admin user can not access the Admin page (403 Forbidden)")
def test_admin_access_denied_for_regular_user(driver):
    with allure.step("Not admin user is logged in"):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(BOB)

        dashboard_page = DashboardPage(driver)
        dashboard_page.assert_that_dashboard_opened()

    with allure.step("Regular user tries to open Admin page with URL"):
        admin_page = AdminPage(driver)
        admin_page.open()

    with allure.step("Assert user is redirected to dashboard page and sees 403 error message"):
        dashboard_page.assert_that_dashboard_opened()
        admin_page.assert_access_denied_toast()
