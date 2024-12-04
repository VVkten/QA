import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="class", autouse=True)
def setup_driver(request):
    """Ініціалізація драйвера з блокуванням реклами"""
    chrome_options = Options()
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--headless")  # Для headless режиму
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get("https://demoqa.com/buttons")
    request.cls.driver = driver
    request.cls.actions = ActionChains(driver)
    yield
    driver.quit()



class TestDemoQAButtons:
    def test_double_click_button(self):
        """Тест 1: Натискання кнопки 'Double Click Me'"""
        double_click_btn = self.driver.find_element(By.XPATH, "//button[text()='Double Click Me']")
        self.actions.double_click(double_click_btn).perform()
        double_click_message = self.driver.find_element(By.ID, "doubleClickMessage")
        assert double_click_message.text == "You have done a double click", \
            f"Очікувано 'You have done a double click', знайдено: '{double_click_message.text}'"

    def test_right_click_button(self):
        """Тест 2: Натискання кнопки 'Right Click Me'"""
        right_click_btn = self.driver.find_element(By.XPATH, "//button[text()='Right Click Me']")
        self.actions.context_click(right_click_btn).perform()
        right_click_message = self.driver.find_element(By.ID, "rightClickMessage")
        assert right_click_message.text == "You have done a right click", \
            f"Очікувано 'You have done a right click', знайдено: '{right_click_message.text}'"

    def test_dynamic_click_button(self):
        """Тест 3: Натискання динамічної кнопки"""
        dynamic_btn = self.driver.find_element(By.XPATH, "//button[text()='Click Me']")
        dynamic_btn.click()
        dynamic_click_message = self.driver.find_element(By.ID, "dynamicClickMessage")
        assert dynamic_click_message.text == "You have done a dynamic click", \
            f"Очікувано 'You have done a dynamic click', знайдено: '{dynamic_click_message.text}'"

    def test_button_exists_with_css(self):
        """Тест 4: Перевірка наявності кнопки 'Double Click Me' за допомогою CSS"""
        assert self.driver.find_element(By.CSS_SELECTOR, "button.btn-primary"), \
            "Кнопка 'Double Click Me' не знайдена!"

    def test_page_header_text(self):
        """Тест 5: Перевірка тексту заголовка сторінки"""
        header = self.driver.find_element(By.XPATH, "//h1[@class='text-center']")
        assert header.text == "Buttons", f"Очікувано заголовок 'Buttons', знайдено: '{header.text}'"

    def test_button_count(self):
        """Тест 6: Перевірка кількості кнопок на сторінці"""
        buttons = self.driver.find_elements(By.XPATH, "//button[@class='btn btn-primary']")
        assert len(buttons) == 3, f"Очікувана кількість кнопок: 3, знайдено: {len(buttons)}"

    def test_button_text_double_click(self):
        """Тест 7: Перевірка тексту кнопки 'Double Click Me'"""
        double_click_btn = self.driver.find_element(By.XPATH, "//button[text()='Double Click Me']")
        assert double_click_btn.text == "Double Click Me", \
            f"Очікувано текст 'Double Click Me', знайдено: '{double_click_btn.text}'"

    def test_button_text_right_click(self):
        """Тест 8: Перевірка тексту кнопки 'Right Click Me'"""
        right_click_btn = self.driver.find_element(By.XPATH, "//button[text()='Right Click Me']")
        assert right_click_btn.text == "Right Click Me", \
            f"Очікувано текст 'Right Click Me', знайдено: '{right_click_btn.text}'"

    def test_button_color(self):
        """Тест 9: Перевірка кольору кнопки 'Click Me'"""
        dynamic_btn = self.driver.find_element(By.XPATH, "//button[text()='Click Me']")
        button_color = dynamic_btn.value_of_css_property("background-color")
        expected_color = "rgba(0, 123, 255, 1)"
        assert button_color == expected_color, f"Очікуваний колір: '{expected_color}', знайдено: '{button_color}'"

    def test_header_font(self):
        """Тест 10: Перевірка шрифту заголовка сторінки"""
        header = self.driver.find_element(By.XPATH, "//h1[@class='text-center']")
        header_font = header.value_of_css_property("font-family")
        expected_font = "Roboto"
        assert expected_font in header_font, f"Очікуваний шрифт: '{expected_font}', знайдено: '{header_font}'"
