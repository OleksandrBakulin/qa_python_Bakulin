'''Написати тести: на сторінці https://demoqa.com/radio-button
А)(test_activate_yes_radio)
Активувати кнопку Yes та переконатись що вона активована.
Переконатись двома різними способами.
Б)(test_get_radio_buttons_info) Визначити які є радіо-баттони на сторінці та сформувати словник із такими даними:
Назва кнопки, Чи увімкнена кнопка, Чи активна (обрана) кнопка.
В (Бонус)(test_activate_disabled_radio_button)
Увімкнути та активувати кнопку No, переконатись в тому, що вона обрана.'''


import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()

@pytest.fixture(scope="module")
def radio_button_page():
    driver.get("https://demoqa.com/radio-button")
    yield driver
    driver.quit()



def test_activate_yes_radio_first(radio_button_page):
    rbutt_yes = driver.find_element(By.XPATH, '//label[@for="yesRadio"]')
    rbutt_yes_input = driver.find_element(By.XPATH, '//input[@id="yesRadio"]')
    rbutt_yes.click()
    result_text = driver.find_element(By.XPATH, '//span[@class="text-success"]').text
    assert all ([result_text == "Yes", rbutt_yes_input.is_enabled()])



def test_get_radio_buttons_info(radio_button_page):
    radio_button_name = driver.find_elements(By.XPATH,'//label[contains(@class, "custom-control")]')
    radio_button_states = driver.find_elements(By.XPATH, '//input[@type="radio"]')
    radio_buttons_dict = {}
    radio_button_count = len(radio_button_name)
    for i in list(range(radio_button_count)):
        radio_buttons_dict.update({radio_button_name[i].text: {'enabled': radio_button_states[i].is_enabled(),
                                                                   'selected': radio_button_states[1].is_selected()}})
    return radio_buttons_dict

def test_activate_disabled_radio_button(radio_button_page):
    rbutt_no_label = driver.find_element(By.XPATH, '//label[@for="noRadio"]')
    rbutt_no_input = driver.find_element(By.XPATH, '//input[@id="noRadio"]')
    driver.execute_script(
        "arguments[0].removeAttribute('disabled','disabled')",rbutt_no_input)
    rbutt_no_label.click()
    assert rbutt_no_input.is_selected()
