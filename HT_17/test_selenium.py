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

NAME_FIELD = '//input[@id="userName"]'
EMAIL_FIELD = '//input[@id="userEmail"]'
CURR_FIELD = '//textarea[@id="currentAddress"]'
PERM_FIELD = '//textarea[@id="permanentAddress"]'
SUBMIT_BUTT = '//button[@id="submit"]'

def test_text_input(text_box):
    name_field = driver.find_element(By.XPATH, NAME_FIELD)
    email_field = driver.find_element(By.XPATH, EMAIL_FIELD)
    current_address_field = driver.find_element(By.XPATH, CURR_FIELD)
    permanent_address_field = driver.find_element(By.XPATH, PERM_FIELD)
    submit_button = driver.find_element(By.XPATH,SUBMIT_BUTT)

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


    if NAME_INPUT != result_name:
        print("\nNames doesnt match")
        i = False
    elif EMAIL_INPUT != result_email:
        print("\nemails doesn't match")
        i = False
    elif CURR_INPUT != result_cur_addr:
        print("\nCurrent addresses doesn't match")
        i = False
    elif PERM_INPUT != result_perm_addr:
        print("\nPermanent addresses doesn't match")
        i = False
    else:
         i = True

    assert i == True

'''XPATH TEST INVALID EMAIL TESS'''
def test_invalid_mail_xpath(text_box):
    email = driver.find_element(By.XPATH, EMAIL_FIELD)
    submit = driver.find_element(By.XPATH, SUBMIT_BUTT)

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