import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


URL = "http://uitestingplayground.com/textinput"

TIME = 2


@pytest.mark.input
def test_input_clear(driver):

    driver.get(URL)
    el = driver.find_element(By.ID, "newButtonName")
    el.send_keys("TEXT")
    button = driver.find_element(By.ID, "updatingButton")
    button.click()
    WebDriverWait(driver, TIME).until(EC.text_to_be_present_in_element(
        (By.ID, "updatingButton"), "TEXT"))

    el.clear()
    assert button.text == "TEXT"


