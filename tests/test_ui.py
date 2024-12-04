# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import pytest
#
# @pytest.fixture
# def setup_driver():
#     """Ініціалізація та закриття браузера"""
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()
#
# def open_google(driver):
#     """Відкриває Google"""
#     driver.get("https://www.google.com")
#
# def search_query(driver, query):
#     """Виконує пошук за заданим запитом"""
#     search = driver.find_element(By.NAME, "q")
#     search.click()
#     search.send_keys(query)
#     search.send_keys(Keys.RETURN)
#
# def click_first_result(driver):
#     """Клікає на перший результат пошуку"""
#     first_result = driver.find_element(By.CSS_SELECTOR, "h3")
#     first_result.click()
#
# def verify_news_title(driver, expected_text):
#     """Перевіряє текст заголовку на сторінці"""
#     news_title_element = driver.find_element(By.CSS_SELECTOR, "h2.border-title.aligncenter.new_title")
#     assert news_title_element.text == expected_text, f"Очікуваний текст '{expected_text}', але знайдено '{news_title_element.text}'"
#
# def test_search_bosco(setup_driver):
#     """Основний тест для перевірки пошуку та заголовку новин"""
#     driver = setup_driver
#     open_google(driver)
#     search_query(driver, "Bosco Lviv")
#     click_first_result(driver)
#     verify_news_title(driver, "НОВИНИ")


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest


def test_search_bosco():
    """Єдиний метод для перевірки пошуку та заголовку новин"""
    # Ініціалізація браузера
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    try:
        # Відкриття Google
        driver.get("https://www.google.com")

        # Виконання пошуку
        search = driver.find_element(By.NAME, "q")
        search.click()
        search.send_keys("Bosco Lviv")
        search.send_keys(Keys.RETURN)

        # Клік на перший результат пошуку
        first_result = driver.find_element(By.CSS_SELECTOR, "h3")
        first_result.click()

        # Перевірка тексту заголовку
        news_title_element = driver.find_element(By.CSS_SELECTOR, "h2.border-title.aligncenter.new_title")
        expected_text = "НОВИНИ"
        assert news_title_element.text == expected_text, f"Очікуваний текст '{expected_text}', але знайдено '{news_title_element.text}'"
    finally:
        # Закриття браузера
        driver.quit()
