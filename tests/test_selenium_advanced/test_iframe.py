import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "http://uitestingplayground.com/frames"


@pytest.mark.iframe
def test_check_iframe(driver):

    driver.get(URL)
    driver.switch_to.frame(driver.find_element(By.ID, "frame-outer"))
    button_edit = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-action="edit"]'))
    )
    button_edit.click()
    result_button = driver.find_element(By.ID, "result")
    assert result_button.text == "Button pressed: Edit"

    driver.switch_to.default_content()
