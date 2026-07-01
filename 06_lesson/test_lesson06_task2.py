import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()

    # Инициализируем WebDriverWait (максимальное ожидание 10 секунд)
    wait = WebDriverWait(driver, 10)

    user_1_cookies = [
        {
            "name": "SESSION",
            "value": "ZWQyZTc0NGUtMDEwZC00NDM3LTg5YzItYTdlYzkwNjYxZjU3",
        },
        {
            "name": "remember-me",
            "value": "R1p0VVltdnlEaUwxOUVIVjZKVEVBQSUzRCUzRDpIT09RNllvVlpRTk9Xa1VROVhiS0Z3JTNEJTNE",
        },
    ]

    user_2_cookies = [
        {
            "name": "SESSION",
            "value": "YjcxOWQ3YjItYzg1Zi00MTYyLWIxZWYtZTg5NjNiOTgwMGZh",
        }
    ]

    try:
        # --- ПОЛЬЗОВАТЕЛЬ 1 ---
        driver.get("https://gitflic.ru/")

        for cookie in user_1_cookies:
            driver.add_cookie(cookie)

        driver.refresh()
        driver.get("https://gitflic.ru/profile")

        # Ждем, пока URL изменится и будет содержать '/profile' (или имя пользователя)
        wait.until(EC.url_contains("profile"))
        url_user_1 = driver.current_url
        print(f"\nURL Пользователя 1: {url_user_1}")

        # Сброс сессии
        driver.delete_all_cookies()

        # --- ПОЛЬЗОВАТЕЛЬ 2 ---
        driver.get("https://gitflic.ru/")

        for cookie in user_2_cookies:
            driver.add_cookie(cookie)

        driver.refresh()
        driver.get("https://gitflic.ru/profile")

        # Снова динамически ждем обновления URL
        wait.until(EC.url_contains("profile"))
        url_user_2 = driver.current_url
        print(f"URL Пользователя 2: {url_user_2}")

        # Проверка
        assert (
                url_user_1 != url_user_2
        ), f"Ошибка: URL пользователей одинаковые! {url_user_1} == {url_user_2}"

    finally:
        driver.quit()


if __name__ == "__main__":
    pytest.main(["-v", "-s", __file__])