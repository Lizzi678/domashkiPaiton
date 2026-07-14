import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from shop_pages import LoginPage, InventoryPage, CartPage, CheckoutPage


@pytest.fixture
def driver():
    # Настраиваем и запускаем Chrome перед тестом
    service = Service(ChromeDriverManager().install())
    chrome_driver = webdriver.Chrome(service=service)
    chrome_driver.maximize_window()

    yield chrome_driver

    # Закрываем браузер после завершения теста
    chrome_driver.quit()


def test_saucedemo_purchase(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # 1. Открыть сайт
    login_page.open()

    # 2. Авторизоваться
    login_page.login("standard_user", "secret_sauce")

    # 3. Добавить товары
    inventory_page.add_backpack()
    inventory_page.add_tshirt()
    inventory_page.add_onesie()

    # 4. В корзину
    inventory_page.go_to_cart()

    # 5. Кнопка Checkout
    cart_page.click_checkout()

    # 6. Заполнить форму доставки твоими данными
    checkout_page.fill_form("Елизавета", "Сушенцова", "630000")

    # 7. Прочитать итоговую сумму
    total_price = checkout_page.get_total_price()

    # 8. Проверить результат
    assert (
        "58.29" in total_price
    ), f"Ожидалась сумма $58.29, но на странице написано: {total_price}"


# Блок для запуска напрямую из PyCharm
if __name__ == "__main__":
    pytest.main(["-v", __file__])