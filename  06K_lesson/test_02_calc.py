import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)

    wait = WebDriverWait(driver, 50)

    try:
        # 1. Открываем страницу калькулятора
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # 2. Находим поле ввода задержки по ID, очищаем и вводим 45
        delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")

        # 3. Нажимаем на кнопки калькулятора
        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        # 4. Локатор экрана калькулятора (класс .screen)
        screen_locator = (By.CSS_SELECTOR, ".screen")

        # Динамическое ожидание появления текста "15" на экране калькулятора
        result_found = wait.until(EC.text_to_be_present_in_element(screen_locator, "15"))

        # Проверка
        assert result_found, "Ошибка: результат '15' не отобразился на экране за отведенное время."

    finally:
        #  закрытие браузера по окончании теста
        driver.quit()


# Строка запуска pytest прямо из кода при запуске файла как скрипта
if __name__ == "__main__":
    pytest.main(["-v", "test_02_calc.py"])