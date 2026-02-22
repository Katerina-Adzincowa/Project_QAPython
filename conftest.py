import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(autouse=False, params=["chrome"])
def driver(request):

    web_driver = None

    if request.param == "firefox":
        opts = FirefoxOptions()
        opts.add_argument("--width=1980")
        opts.add_argument("--height=1600")
        web_driver = webdriver.Firefox(options=opts)

    else:
        opts = Options()
        # opts.add_argument("--headless=new")
        opts.add_argument("--incognito")
        opts.add_argument("--window-size=1980,1600")
        opts.add_argument("--ignore-certificate-errors")
        opts.add_argument("--allow-running-insecure-content")

        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        }
        opts.add_experimental_option("prefs", prefs)

        web_driver = webdriver.Chrome(options=opts)
        # web_driver.maximize_window()
        web_driver.implicitly_wait(5)

    yield web_driver
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
        driver.execute_cdp_cmd("Page.setDownloadBehavior", {"behavior": "deny"})

    assert driver.current_url.endswith("/dashboard")
