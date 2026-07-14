from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

        self._delay_input = (By.CSS_SELECTOR, "#delay")
        self._button_7 = (By.XPATH, "//span[text()='7']")
        self._button_plus = (By.XPATH, "//span[text()='+']")
        self._button_8 = (By.XPATH, "//span[text()='8']")
        self._button_equal = (By.XPATH, "//span[text()='=']")
        self._result = (By.CSS_SELECTOR, ".screen")

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, delay_value):
        delay_field = self.driver.find_element(*self._delay_input)
        delay_field.clear()
        delay_field.send_keys(str(delay_value))

    def click_7(self):
        self.driver.find_element(*self._button_7).click()

    def click_plus(self):
        self.driver.find_element(*self._button_plus).click()

    def click_8(self):
        self.driver.find_element(*self._button_8).click()

    def click_equal(self):
        self.driver.find_element(*self._button_equal).click()

    def get_result(self, timeout=50):
        # Ждем, пока на экране (.screen) появится итоговое значение "15"
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self._result, "15")
        )
        return self.driver.find_element(*self._result).text