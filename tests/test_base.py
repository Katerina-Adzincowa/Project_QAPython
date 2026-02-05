import time

from selenium.webdriver.common.by import By

BASE_URL = "http://localhost:3000"
SUBSCRIPTION = f"{BASE_URL}/automation-lab/subscription"
CARDS = f"{BASE_URL}/automation-lab/cards"


def test_open_card(driver):
    print("\n+++Запустили тест 'test_open_card'+++")
    driver.get(CARDS)
    time.sleep(5)
    assert driver.title == "Task Management Board"
    assert driver.current_url == CARDS


def test_open_subscription_fixture(driver):
    print("\n+++Запустили тест 'test_open_subscription_fixture'+++")
    driver.get(SUBSCRIPTION)
    time.sleep(5)
    assert driver.title == "Task Management Board"
    assert driver.current_url == SUBSCRIPTION

    element_payment_section = driver.find_element(By.CSS_SELECTOR, ".payment-section")
    assert element_payment_section.is_displayed()
