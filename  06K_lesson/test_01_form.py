from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_fill_form():
    options = webdriver.EdgeOptions()
    options.add_experimental_option(
        "prefs",
        {
            "intl.accept_languages": "en,en-US",
        },
    )

    driver = webdriver.Edge(
        service=EdgeService(EdgeChromiumDriverManager().install()),
        options=options,
    )

    # 1. Открываем оригинальный сайт
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )
    driver.maximize_window()

    # Проверенные локаторы по DOM-дереву
    form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "city": "Москва",
        "country": "Россия",
        "e-mail": "test@skypro.com",
        "phone": "+79858999987",
        "job-position": "QA",
        "company": "SkyPro",
    }

    # 2. Заполняем все поля из словаря
    for name, value in form_data.items():
        field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, name))
        )
        field.clear()

        # Для стабильности ввода телефона и почты используем посимвольный ввод
        if name in ["phone", "e-mail"]:
            for char in value:
                field.send_keys(char)
                time.sleep(0.05)  # Небольшая пауза, чтобы браузер успевал прожевать цифры
        else:
            field.send_keys(value)

    # Поле Почтовый индекс (name="zip-code") намеренно оставляем пустым

    # 3. Кликаем по кнопке Submit
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    submit_button.click()

    # 4. Проверяем, что Zip-code подсветился красным
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element_attribute(
            (By.NAME, "zip-code"), "class", "alert-danger"
        )
    )
    zip_field = driver.find_element(By.NAME, "zip-code")
    assert "alert-danger" in zip_field.get_attribute(
        "class"
    ), "Поле Zip code не подсвечено красным!"

    # 5. Проверяем, что остальные поля стали зелеными
    for name in form_data.keys():
        field = driver.find_element(By.NAME, name)
        assert "alert-success" in field.get_attribute(
            "class"
        ), f"Поле {name} не подсвечено зеленым!"

    # Закрываем сессию браузера
    driver.quit()


if __name__ == "__main__":
    import pytest

    pytest.main(["-v", __file__])