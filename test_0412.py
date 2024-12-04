from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/buttons")
time.sleep(3)

actions = ActionChains(driver)

# Тест 1: Натискання кнопки "Double Click Me"
double_click_btn = driver.find_element(By.XPATH, "//button[text()='Double Click Me']")
actions.double_click(double_click_btn).perform()
time.sleep(2)
double_click_message = driver.find_element(By.ID, "doubleClickMessage")
assert double_click_message.text == "You have done a double click", \
    f"Очікувано 'You have done a double click', знайдено: '{double_click_message.text}'"

# Тест 2: Натискання кнопки "Right Click Me"
right_click_btn = driver.find_element(By.XPATH, "//button[text()='Right Click Me']")
actions.context_click(right_click_btn).perform()
time.sleep(2)
right_click_message = driver.find_element(By.ID, "rightClickMessage")
assert right_click_message.text == "You have done a right click", \
    f"Очікувано 'You have done a right click', знайдено: '{right_click_message.text}'"

# Тест 3: Натискання динамічної кнопки
dynamic_btn = driver.find_element(By.XPATH, "//button[text()='Click Me']")
dynamic_btn.click()
time.sleep(2)
dynamic_click_message = driver.find_element(By.ID, "dynamicClickMessage")
assert dynamic_click_message.text == "You have done a dynamic click", \
    f"Очікувано 'You have done a dynamic click', знайдено: '{dynamic_click_message.text}'"

# Тест 4: Перевірка наявності кнопки "Double Click Me" за допомогою CSS
assert driver.find_element(By.CSS_SELECTOR, "button.btn-primary"), "Кнопка 'Double Click Me' не знайдена!"

# Тест 5: Перевірка тексту заголовка сторінки
header = driver.find_element(By.XPATH, "//h1[@class='text-center']")
assert header.text == "Buttons", f"Очікувано заголовок 'Buttons', знайдено: '{header.text}'"

# Тест 6: Перевірка кількості кнопок на сторінці
buttons = driver.find_elements(By.XPATH, "//button[@class='btn btn-primary']")
assert len(buttons) == 3, f"Очікувана кількість кнопок: 3, знайдено: {len(buttons)}"

# Тест 7: Перевірка тексту кнопки "Double Click Me"
assert double_click_btn.text == "Double Click Me", \
    f"Очікувано текст 'Double Click Me', знайдено: '{double_click_btn.text}'"

# Тест 8: Перевірка тексту кнопки "Right Click Me"
assert right_click_btn.text == "Right Click Me", \
    f"Очікувано текст 'Right Click Me', знайдено: '{right_click_btn.text}'"

# Тест 9: Перевірка кольору кнопки "Click Me"
button_color = dynamic_btn.value_of_css_property("background-color")
expected_color = "rgba(0, 123, 255, 1)"  # Синій колір у CSS
assert button_color == expected_color, f"Очікуваний колір: '{expected_color}', знайдено: '{button_color}'"

# Тест 10: Перевірка шрифту заголовка сторінки
header_font = header.value_of_css_property("font-family")
expected_font = "Roboto"
assert expected_font in header_font, f"Очікуваний шрифт: '{expected_font}', знайдено: '{header_font}'"

# Закриття браузера
driver.quit()
