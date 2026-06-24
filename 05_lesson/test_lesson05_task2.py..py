from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_submission():
    # Инициализация драйвера
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # 1. Заходим на страницу
        driver.get("https://httpbin.org/forms/post")

        # 2. Ввод данных
        wait = WebDriverWait(driver, 10)
        name_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="custname"]')))
        name_field.send_keys("Елизавета")

        # 3. Клик
        submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit order')]")
        submit_button.click()

        # 4. Ожидание результата
        wait.until(EC.url_to_be("https://httpbin.org/post"))

        # 5. Проверка
        body_text = driver.find_element(By.TAG_NAME, "body").text
        decoded_text = body_text.encode('utf-8').decode('unicode-escape')
        assert "Елизавета" in decoded_text, "Ошибка: имя не найдено!"

        print("Тест пройден успешно!")

    finally:

        driver.quit()


if __name__ == "__main__":
    test_form_submission()