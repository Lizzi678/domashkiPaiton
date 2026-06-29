from selenium import webdriver
from selenium.webdriver.common.by import By

def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/links/10")

    # 1. Находим все ссылки (тег <a>)
    links = driver.find_elements(By.TAG_NAME, "a")

    # 2. Проверяем, что количество ссылок равно 9
    assert len(links) == 9, f"Ожидалось 9 ссылок, а найдено {len(links)}"

    # 3. Проверяем, что все ссылки отображаются (is_displayed)
    for link in links:
        assert link.is_displayed(), f"Ссылка {link.get_attribute('href')} не отображается"

    # 4. Проверяем, что текст первой ссылки содержит "1"
    # Используем индекс [0] для обращения к первому элементу списка
    first_link_text = links[0].text
    assert "1" in first_link_text, f"Текст первой ссылки '{first_link_text}' не содержит '1'"

    print("Все проверки пройдены успешно!")
    driver.quit()

if __name__ == "__main__":
    test_multiple_elements()