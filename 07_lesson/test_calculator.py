import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    # Настраиваем и запускаем Chrome перед тестом
    service = Service(ChromeDriverManager().install())
    chrome_driver = webdriver.Chrome(service=service)
    chrome_driver.maximize_window()

    yield chrome_driver

    # Закрываем браузер после завершения теста
    chrome_driver.quit()


def test_slow_calculator(driver):
    # Инициализируем нашу страницу, передавая ей драйвер
    calc_page = CalculatorPage(driver)

    # 1. Открываем страницу калькулятора
    calc_page.open()

    # 2. Вводим значение 45 в поле задержки
    calc_page.set_delay(45)

    # 3. Нажимаем последовательно кнопки: 7, +, 8, =
    calc_page.click_7()
    calc_page.click_plus()
    calc_page.click_8()
    calc_page.click_equal()

    # 4. Получаем результат работы калькулятора
    # Метод get_result сам подождет нужные 45 секунд
    result = calc_page.get_result(timeout=50)

    # 5. Проверяем, что на экране отобразилось число 15
    assert result == "15", f"Ожидался результат 15, но калькулятор показал: {result}"

