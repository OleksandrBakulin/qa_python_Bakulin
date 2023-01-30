'''
1. Написати тест test_checkboxes: на сторінці https://demoqa.com/checkbox обрати (поставити галочку) 2 елемента:
Commands (Home-Desktop) та General (Home-Documents-Office).
Обирати елементи потрібно однією функцією, по імені елеемнта.
Як бонусне завдання: реалізувати метод так, щоб він міг прймати масив назв елементів як аргумент і розкривати список послідовно.
'''

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()


@pytest.fixture()
def check_box_page():
    driver.get("https://demoqa.com/checkbox")

def test_check_box(check_box_page):
    checkbox_finder('Desktop')
    checkbox_finder('Office')


def checkbox_finder(element_name: str,):
    tree_opener = driver.find_element(By.XPATH,'//button[contains(@class, "expand-all")]')
    tree_opener.click()

    checkbox_list_names = []
    box_list = []
    box_list = driver.find_elements(By.XPATH, '//span[contains(@class,"rct-title")]')
    for e in box_list:
        checkbox_list_names.append(e.text)
        if e.text == element_name:
            enabler = driver.find_element(By.XPATH, '//ancestor::label/span[@class="rct-checkbox"]')
            enabler.click()

