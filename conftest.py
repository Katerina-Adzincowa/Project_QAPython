
import time
import allure
import pytest
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions

BASE_DIR = Path(__file__).resolve().parent


def pytest_addoption(parser):
    parser.addoption("--br", action="store", default="chrome", help="the name of the browser")
    parser.addoption("--allure-print", action="store_true", default=True)
    parser.addoption("--locale", action="store", default="en")


@pytest.fixture(scope="session")
def locale(pytestconfig):
    return pytestconfig.getoption("--locale")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(autouse=False)
def driver(request, pytestconfig):
    browser = pytestconfig.getoption("--br")

    if browser == "firefox":
        opts = FirefoxOptions()
        opts.add_argument("--width=1980")
        opts.add_argument("--height=1600")
        web_driver = webdriver.Firefox(options=opts)
    else:
        # Ваши настройки Chrome с путями
        opts = Options()
        opts.add_argument("--incognito")
        opts.add_argument("--window-size=1980,1600")
        opts.add_argument("--ignore-certificate-errors")
        opts.add_argument("--allow-running-insecure-content")

        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
            "download.default_directory": str(BASE_DIR / "files"),
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": False,
        }
        opts.add_experimental_option("prefs", prefs)
        web_driver = webdriver.Chrome(options=opts)
        web_driver.implicitly_wait(10)

    yield web_driver

    report = getattr(request.node, "rep_call", None)
    if report:
        try:
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
            allure.attach(
                web_driver.current_url,
                name="Current url",
                attachment_type=allure.attachment_type.URI_LIST,
            )
        except Exception as e:
            print(f"Failed to attach: {e}")

    web_driver.quit()


@pytest.fixture()
def login(driver):
    URL = "http://localhost:3000/login"
    driver.get(URL)

    email = driver.find_element(By.CSS_SELECTOR, '[data-qa="login-email-input"]')
    password = driver.find_element(By.CSS_SELECTOR, '[data-qa="login-password-input"]')
    submit = driver.find_element(By.CLASS_NAME, "btn-primary")

    email.send_keys("bob@example.com")
    password.send_keys("password123")
    submit.click()

    time.sleep(2)

    if driver.name == "chrome":
        driver.execute_cdp_cmd("Page.setDownloadBehavior", {
            "behavior": "allow",
            "downloadPath": str(BASE_DIR / "files")
        })

    assert driver.current_url.endswith("/dashboard")
