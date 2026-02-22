import pytest
from selenium.webdriver.common.by import By

URL = "http://localhost:3000/automation-lab/subscription"


@pytest.mark.filling_out_card
def test_filling_out_card(driver):
    driver.get(URL)

    card_number = driver.find_element(By.CSS_SELECTOR, '[data-testid="card-number"]')
    card_number.click()
    card_number.send_keys("5555 5555 5555 4444")

    bank_element = driver.find_element(By.CLASS_NAME, 'card-brand')
    assert bank_element.is_displayed()

    expiry = driver.find_element(By.CSS_SELECTOR, '[data-testid="card-expiry"]')
    expiry.click()
    expiry.send_keys("062026")

    cvv = driver.find_element(By.CSS_SELECTOR, '[data-testid="card-cvv"]')
    cvv.click()
    cvv.send_keys("322")

    button = driver.find_element(By.CLASS_NAME, 'cvv-toggle')
    button.click()

    actual_cvv = cvv.get_attribute("value")
    assert actual_cvv == "322"
