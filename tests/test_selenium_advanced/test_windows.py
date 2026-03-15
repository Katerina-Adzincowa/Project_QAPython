import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://letcode.in/window"


@pytest.mark.windows
def test_windows(driver):
    driver.get(URL)
    main_window = driver.current_window_handle
    driver.find_element(By. ID, "multi").click()
    WebDriverWait(driver, 5).until(
        EC.number_of_windows_to_be(3)
    )
    all_windows = driver.window_handles
    assert len(all_windows) == 3

    driver.switch_to.window(all_windows[-2])
    assert driver.current_url == "https://letcode.in/alert"
    breakpoint()
    driver.close()
    driver.switch_to.window(all_windows[-1])
    assert driver.current_url == "https://letcode.in/dropdowns"

    driver.close()
    driver.switch_to.window(main_window)
    assert driver.current_url == URL
