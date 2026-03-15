import pytest
from selenium.webdriver.common.by import By


URL = "http://localhost:3000/automation-lab/subscription"


ALL_COMBO = [

    ('[data-testid="period-1"]', '[data-testid="tariff-basic"]'),
    ('[data-testid="period-1"]', '[data-testid="tariff-premium"]'),
    ('[data-testid="period-1"]', '[data-testid="tariff-family"]'),


    ('[data-testid="period-3"]', '[data-testid="tariff-basic"]'),
    ('[data-testid="period-3"]', '[data-testid="tariff-premium"]'),
    ('[data-testid="period-3"]', '[data-testid="tariff-family"]'),


    ('[data-testid="period-12"]', '[data-testid="tariff-basic"]'),
    ('[data-testid="period-12"]', '[data-testid="tariff-premium"]'),
    ('[data-testid="period-12"]', '[data-testid="tariff-family"]'),
]


@pytest.mark.period_plan
@pytest.mark.parametrize("period_selector, plan_selector", ALL_COMBO)
def test_period_plus_plan(driver, period_selector, plan_selector):

    driver.get(URL)
    period_button = driver.find_element(By.CSS_SELECTOR, period_selector)
    period_button.click()
    plan_button = driver.find_element(By.CSS_SELECTOR, plan_selector)
    plan_button.click()

    assert "active" in period_button.get_attribute("class")
    assert "selected" in plan_button.get_attribute("class")
