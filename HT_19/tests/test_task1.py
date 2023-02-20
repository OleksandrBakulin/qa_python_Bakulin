'''"Reuse fixture yield data": Створити 2 фікстури. Нехай одна буде створювати headless драйвер
(На ваш вибір: Chrome/Chromium/Edge, Firefox), а інша буде використовуючи цей драйвер відкривати сторінку
https://demoqa.com/links та закривати драйвер після тесту. Створити тест, який переконається, що на сторінці є 2 посилання з текстом "Home".
Не викликати ЯВНО фікстуру в тесті (сигнатура тестової функції має бути пуста).'''
import pytest
from selenium.webdriver.common.by import By

home_links = []

@pytest.fixture(scope='function', autouse=True)
def links_page(driver):
    driver.get('https://demoqa.com/links')
    home_links = driver.find_elements(By.PARTIAL_LINK_TEXT, 'Home')
    yield driver

class Linktest:
    def __init__(self,driver):
        self.driver = driver

    def test_home_links():
        assert len(home_links) == 2

