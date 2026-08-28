import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_saucedemo_shop():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)

    # Ожидание элементов до 10 секунд
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Открываем сайт магазина
        driver.get("https://www.saucedemo.com/")

        # 2. Авторизуемся под standard_user
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#user-name"))).send_keys("standard_user")
        driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        driver.find_element(By.CSS_SELECTOR, "#login-button").click()

        # 3. Добавляем в корзину три выбранных товара (используем проверенные уникальные ID кнопок)
        # Товар 1: Sauce Labs Backpack
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"))).click()

        # Товар 2: Sauce Labs Bolt T-Shirt
        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()

        # Товар 3: Sauce Labs Onesie
        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

        # 4. Переходим в корзину (Локатор иконки корзины)
        driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

        # 5. Нажимаем Checkout (Локатор кнопки оформления)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout"))).click()

        # 6. Заполняем форму своими данными (Локаторы полей ввода по ID)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#first-name"))).send_keys("Иван")
        driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Иванов")
        driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("123456")

        # 7. Нажимаем кнопку Continue (Локатор кнопки продолжения по ID)
        driver.find_element(By.CSS_SELECTOR, "#continue").click()

        # 8. Читаем со страницы итоговую стоимость
        total_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".summary_total_label")))
        total_text = total_element.text  # Получаем строку вида "Total: $58.29"

        # 9. Проверяем, что итоговая сумма равна $58.29
        assert "$58.29" in total_text, f"Ожидалась сумма $58.29, но на странице отображено: '{total_text}'"

    finally:
        driver.quit()


if __name__ == "__main__":
    pytest.main(["-v", "test_03_shop.py"])