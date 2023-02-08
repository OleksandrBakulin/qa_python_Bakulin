'''Написати тести: на сторінці https://demoqa.com/dynamic-properties
А)(test_get_id) використовуючи фікстуру отримати ID рядка "This text has random Id".
В тесті використовуючи отриманий фікстурою ID, сформувати веб-елемент, та отримати його текст.
Переконатись, що в отриманому рядку є слово random.
Б)(test_wait_for_enable_element) Переконатись, що кнопка "Will enable 5 seconds" увімкнена, попередньо дочекавшись цього.
Не використовувати time.sleep() напряму.
Бонус: написати власний метод, розумного очікування якогось стану елемента, на ваш розсуд. На
приклад, що елемент увімкнений.
В)(test_button_is_present) Оновити сторінку та переконатись що кнопка "Visible After 5 Seconds" стала видимою на сторінці.
 Не використовувати time.sleep() напряму.'''
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = Chrome()


@pytest.fixture(scope="module")
def dynamic_prop():
    driver.get("https://demoqa.com/dynamic-properties")
    yield driver
    driver.quit()

@pytest.fixture()
def id_cacth():
    idcatch = driver.find_element(By.XPATH, '//p[text()="This text has random Id"]')
    yield idcatch.get_attribute('id')

def test_get_id(dynamic_prop,id_cacth):
    id_web_elemnt = driver.find_element(By.XPATH, f'//p[@id="{id_cacth}"]')
    assert "random" in id_web_elemnt.text

def test_wait_for_enable_element(dynamic_prop):
    locator = (By.XPATH, '//button[@id="enableAfter"]')
    WebDriverWait(dynamic_prop, timeout=6).until(expected_conditions.element_to_be_clickable(locator))
    button_enable_five = driver.find_element(*locator)
    assert button_enable_five.is_enabled()

def test_button_is_present(dynamic_prop):
    driver.implicitly_wait(20)
    button_visible = driver.find_element(By.XPATH, '//button[@id="visibleAfter"]')
    assert button_visible.is_enabled()

