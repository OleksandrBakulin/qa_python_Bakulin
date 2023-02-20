import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()


@pytest.fixture()
def checkbox_page():
    driver.get("https://demoqa.com/checkbox")

@pytest.fixture()
def radio_button_page():
    driver.get("https://demoqa.com/radio-button")


def test_checkbox_1(checkbox_page):
    set_checkbox_state("Home", enabled=True)
    pass
#

def set_checkbox_state(folder_name: str, enabled: bool = True) -> None:
    folder = driver.find_element(
        By.XPATH,
        f'//span[@class="rct-title"][.="{folder_name}"]'
        f'//ancestor::span[@class="rct-text"]')
    fold_input = folder.find_element(By.CSS_SELECTOR, 'input[id]')
    fold_checkbox = folder.find_element(By.CSS_SELECTOR, 'label[for]')
    if enabled:
        if not fold_input.is_selected():
            fold_checkbox.click()
        else:
            if fold_input.is_selected():
                fold_checkbox.click()

#
# def test_radio_button(radio_button_page):
#     label_yes = driver.find_element(By.XPATH, '//label[@for="yesRadio"]')
#     input_yes = driver.find_element(By.XPATH, '//input[@id="yesRadio"]')
#
#     label_impressive = driver.find_element(By.XPATH, '//label[@for="impressiveRadio"]')
#     input_impressive = driver.find_element(By.XPATH, '//input[@id="impressiveRadio"]')
#
#     pass


