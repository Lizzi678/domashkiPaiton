from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep  # Добавили импорт sleep


def test_navigation1():
    driver = webdriver.Chrome()
    try:
        # 1. Открыть страницу
        driver.get("https://automationexercise.com/")
        driver.maximize_window()
        sleep(2)

        # 2. Кликнуть на "Продукты"
        driver.find_element(By.XPATH, "//a[@href='/products']").click()
        sleep(5)

        # 3. Работа с поиском
        search_field = driver.find_element(By.ID, "search_product")
        search_field.send_keys("Ваш товар")
        sleep(2)

        # 4. Возврат на главную
        # Находим и кликаем
        home_button = driver.find_element(By.XPATH, "//ul[@class='nav navbar-nav']//a[@href='/']")
        home_button.click()

        print("Тест успешно завершен: переход на главную выполнен.")
        sleep(5)

    finally:
        # 5. Правильное завершение
        driver.quit()


# Запуск функции
if __name__ == "__main__":
    test_navigation1()