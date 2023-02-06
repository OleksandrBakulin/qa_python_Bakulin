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

def test_checkboxes(check_box_page):
    names = ["Commands","General"]
    folder_tree = ["Home", "Desktop", "Documents", "WorkSpace", "Office", "Downloads"]
    for i in folder_tree:
        exp = driver.find_element(By.XPATH,
                                  f'//span[@class="rct-text"][.="{i}"]/button[@aria-label="Toggle"]')
        exp.click()
    for i in names:
        checkbox_selected_text(i)
    checkboxes_text = driver.find_element(By.XPATH, '//div[@id="result"]').text.split(":")[1].split()
    results = list(map(lambda x: x.lower(), names))
    assert results == checkboxes_text

def checkbox_selected_text(element_name: str, enabled : bool = True):

    checkbox_list_names = []
    box_list = driver.find_elements(By.XPATH, '//span[contains(@class,"rct-title")]')
    for e in box_list:
        checkbox_list_names.append(e.text)
        if e.text == element_name:
            enabler = driver.find_element(By.XPATH,
            f'//span[@class="rct-title"][.="{element_name}"]'
            f'//ancestor::span[@class="rct-text"]')
            output_element = driver.find_element(By.XPATH, f'//span[@class="rct-title"][.="{element_name}"]')
            output_element.location_once_scrolled_into_view
            element_input = enabler.find_element(By.CSS_SELECTOR, "input[id]")

            if enabled:
                if not element_input.is_selected():
                    enabler.click()
            else:
                if element_input.is_selected():
                    enabler.click()


