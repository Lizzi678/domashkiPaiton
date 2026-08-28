import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        start_button = driver.find_element(By.XPATH, "//div[@id='start']/button")
        start_button.click()

        wait = WebDriverWait(driver, 10)
        finish_text_element = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[@id='finish']/h4"))
        )

        current_dir = os.path.dirname(os.path.abspath(__file__))
        screenshot_dir = os.path.join(current_dir, "screenshot")

        os.makedirs(screenshot_dir, exist_ok=True)

        screenshot_path = os.path.join(screenshot_dir, "result_screenshot.png")

        driver.save_screenshot(screenshot_path)

        actual_text = finish_text_element.text
        assert actual_text == "Hello World!", f"Ожидался текст 'Hello World!', но пришел '{actual_text}'"

    finally:
        driver.quit()


if __name__ == "__main__":
    test_dynamic_loading()