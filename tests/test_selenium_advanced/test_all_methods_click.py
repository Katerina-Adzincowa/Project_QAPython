import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


URL = "http://uitestingplayground.com/click"


@pytest.mark.usual_click
def test_usual_click(driver):
    driver.get(URL)
    driver.find_element(By.ID, "badButton").click()
    breakpoint()


@pytest.mark.js_click
def test_js_click(driver):
    driver.get(URL)
    el = driver.find_element(By.ID, "badButton")
    driver.execute_script("arguments[0].click();", el)
    breakpoint()


@pytest.mark.action_chains_click
def test_action_chains_click(driver):
    driver.get(URL)
    el = driver.find_element(By.ID, "badButton")
    ActionChains(driver).click(el).perform()
    breakpoint()


@pytest.mark.send_keys_click
def test_send_keys_click(driver):
    driver.get(URL)
    el = driver.find_element(By.ID, "badButton")
    el.send_keys(Keys.ENTER)

