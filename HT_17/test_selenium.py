import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


driver = Chrome()

@pytest.fixture()
def text_box():
    driver.get("https://demoqa.com/text-box")

NAME_INPUT = "Alex"
EMAIL_INPUT = 'mymail@gmail.com'
CURR_INPUT = "Rivne, Shevchenka"
PERM_INPUT = "Kharkiv, Shevchenka"

def test_text_input(text_box):
    name_field = driver.find_element(By.XPATH, '//input[@id="userName"]')
    email_field = driver.find_element(By.XPATH, '//input[@id="userEmail"]')
    current_address_field = driver.find_element(By.XPATH, '//textarea[@id="currentAddress"]')
    permanent_address_field = driver.find_element(By.XPATH, '//textarea[@id="permanentAddress"]')
    submit_button = driver.find_element(By.XPATH, '//button[@id="submit"]')

    name_field.send_keys(NAME_INPUT)
    email_field.send_keys(EMAIL_INPUT)
    current_address_field.send_keys(CURR_INPUT)
    permanent_address_field.send_keys(PERM_INPUT)
    submit_button.click()

    output_element = driver.find_element(By.ID, "output")
    output_element.location_once_scrolled_into_view


    result_name = name_field.find_element(By.XPATH, '//p[@id="name"]').text.split(sep=":")[1]
    result_email = email_field.find_element(By.XPATH, '//p[@id="email"]').text.split(sep=":")[1]
    result_cur_addr = current_address_field.find_element(By.XPATH, '//p[@id="currentAddress"]').text.split(sep=":")[1]
    result_perm_addr = permanent_address_field.find_element(By.XPATH, '//p[@id="permanentAddress"]').text.split(sep=":")[1]


    assert NAME_INPUT == result_name
    assert EMAIL_INPUT == result_email
    assert CURR_INPUT == result_cur_addr
    assert PERM_INPUT == result_perm_addr


'''XPATH TEST INVALID EMAIL TESS'''
def test_invalid_mail_xpath(text_box):
    email = driver.find_element(By.XPATH, '//input[@id="userEmail"]')
    submit = driver.find_element(By.XPATH, '//button[@id="submit"]')

    email.send_keys('mymailgmailom')
    submit.click()

    red_field = driver.find_element(By.XPATH, '//input[@type="email"][contains(@class, "error")]')
    assert red_field

'''CCS SELECTOR INVALID EMAIL TESS'''
def test_invalid_mail_css(text_box):

    email = driver.find_element(By.CSS_SELECTOR, '#userEmail')
    submit = driver.find_element(By.CSS_SELECTOR, '#submit')


    email.send_keys('mymailgmailom')
    submit.click()

    red_field = driver.find_element(By.CSS_SELECTOR, '[class~=field-error]')
    assert red_field