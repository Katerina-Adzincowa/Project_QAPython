import time
import pytest
from conftest import BASE_DIR
from selenium.webdriver.common.by import By

URL = "https://letcode.in/file"


@pytest.mark.upload
def test_upload(driver):
    driver.get(URL)
    file_path = str(BASE_DIR / "files" / "sample.txt")
    driver.find_element(By.CSS_SELECTOR, ".file-input").send_keys(file_path)
    time.sleep(2)

    message = driver.find_element(By.CSS_SELECTOR, '.label.ng-star-inserted')
    assert message.is_displayed()
    assert "sample.txt" in message.text


@pytest.mark.download
def test_download(driver):
    driver.get(URL)
    driver.find_element(By.XPATH, '//a[@id="txt"]').click()
    time.sleep(2)

    assert driver.current_url == URL
    assert driver.find_element(By.XPATH, '//a[@id="txt"]').is_displayed()
