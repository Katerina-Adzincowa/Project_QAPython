import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


URL = "http://uitestingplayground.com/alerts"

TIME = 5


def wait_for_alert(driver):
    return WebDriverWait(driver, TIME).until(EC.alert_is_present())


@pytest.mark.alerts
def test_alert(driver):

    driver.get(URL)
    driver.find_element(By.ID, "alertButton").click()
    alert = wait_for_alert(driver)
    assert alert.text == "Today is a working day.\nOr less likely a holiday."

    alert.accept()

    assert "/alerts" in driver.current_url
