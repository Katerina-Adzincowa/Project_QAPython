import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

BASE_URL = "http://localhost:3000"
LABCARDS = f"{BASE_URL}/automation-lab/cards"

def test_open_labcards():
    opts = Options()
    #opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1980,1600")
    driver = webdriver.Chrome(options=opts)

    driver.get(LABCARDS)

    assert driver.title == "Task Management Board"
    assert driver.current_url == LABCARDS
    breakpoint()
    button_view_task_section = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    assert button_view_task_section.is_displayed()
