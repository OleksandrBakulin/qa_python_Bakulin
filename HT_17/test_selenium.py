import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


driver = Chrome()

@pytest.fixture()
def text_box():
    driver.get("https://demoqa.com/text-box")

def test_text_input(text_box):
    name = driver.find_element(By.XPATH, '//input[@id="userName"]')
    email = driver.find_element(By.XPATH, '//input[@id="userEmail"]')
    current_adress = driver.find_element(By.XPATH, '//textarea[@id="currentAddress"]')
    permanent_adress = driver.find_element(By.XPATH, '//textarea[@id="permanentAddress"]')
    submit = driver.find_element(By.XPATH, '//button[@id="submit"]')

    name.send_keys("Alex")
    email.send_keys('mymail@gmail.com')
    current_adress.send_keys("Rivne, Shevchenka")
    permanent_adress.send_keys("Kharkiv, Shevchenka")
    submit.click()

    output_element = driver.find_element(By.ID, "output")
    output_element.location_once_scrolled_into_view

    name_value = name.get_attribute("value")
    email_value = email.get_attribute("value")
    curr_addr_value = current_adress.get_attribute('value')
    perm_addr_value = permanent_adress.get_attribute('value')

    result_name = name.find_element(By.XPATH, '//p[@id="name"]').text[5:]
    result_email = email.find_element(By.XPATH, '//p[@id="email"]').text[6:]
    result_cur_addr = current_adress.find_element(By.XPATH, '//p[@id="currentAddress"]').text[17:]
    result_perm_addr = permanent_adress.find_element(By.XPATH, '//p[@id="permanentAddress"]').text[20:]

    assert name_value == result_name
    assert email_value == result_email
    assert curr_addr_value == result_cur_addr
    assert perm_addr_value == result_perm_addr

'''XPATH TEST INVALID EMAIL TESS'''
def test_invalid_mail_xpath(text_box):
    email = driver.find_element(By.XPATH, '//input[@id="userEmail"]')
    submit = driver.find_element(By.XPATH, '//button[@id="submit"]')
    normal_field = driver.find_element(By.XPATH, '//input[@class="mr-sm-2 form-control"]')

    assert normal_field
    email.send_keys('mymailgmailom')
    submit.click()

    red_field = driver.find_element(By.XPATH, '//input[@class="mr-sm-2 field-error form-control"]')
    assert red_field
'''CCS SELECTOR INVALID EMAIL TESS'''
def test_invalid_mail_css(text_box):

    email = driver.find_element(By.CSS_SELECTOR, 'input[type="email"]')
    submit = driver.find_element(By.CSS_SELECTOR, 'button[id="submit"]')
    normal_field = driver.find_element(By.CSS_SELECTOR, 'input[class="mr-sm-2 form-control"]')
    assert normal_field

    email.send_keys('mymailgmailom')
    submit.click()

    red_field = driver.find_element(By.CSS_SELECTOR, 'input[class="mr-sm-2 field-error form-control"]')
    assert red_field