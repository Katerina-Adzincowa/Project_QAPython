import pytest
from selenium.webdriver.common.by import By


URL = "http://localhost:3000/automation-lab/subscription"


@pytest.mark.parametrize("promo, expected_message", [
    ("WELCOME10", "Промокод истек"),
    ("SUMMER25", "Промокод истек"),
    ("LOYALTY15", "Промокод истек"),
    ("@#$%", "Промокод не найден"),
])
@pytest.mark.inv
def test_invalid_promo(driver, promo, expected_message):
    driver.maximize_window()
    driver.get(URL)

    period_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="period-12"]')
    period_button.click()

    premium_button = driver.find_element(By.CSS_SELECTOR, '[data-tariff="premium"]')
    premium_button.click()

    inp = driver.find_element(By.CSS_SELECTOR, '[data-testid="promo-input"]')
    inp.clear()
    inp.send_keys(promo)

    apply_btn = driver.find_element(By.CLASS_NAME, "promo-apply-btn")
    driver.execute_script("arguments[0].click();", apply_btn)

    message = driver.find_element(By.CSS_SELECTOR, '[data-testid="promo-message"]')
    assert message.is_displayed()
    actual_text = message.text
    assert expected_message in actual_text
