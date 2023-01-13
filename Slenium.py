from selenium.webdriver.common.by import By

FULL_NAME_FIELD = '//input[@id="userName"]'
EMAIL_FIELD = '//input[@id="userName"]'
CURRENT_ADDRESS = '//textarea[@id="currentAddress"]'
PERM_ADDR_FIELD = '//textarea[@id="id="permanentAddress"]'
SUBMIT_BUTTON = '//button[@id=submit"]'


def test_text_boxes1(chrome):
    driver = chrome
    driver.get("https://demoqa.com/text-box")
    name = driver.find_element(By.XPATH, FULL_NAME_FIELD)
    email = driver.find_element(By.XPATH, EMAIL_FIELD)
    current_adress = driver.find_element(By.XPATH, CURRENT_ADDRESS)
    permanent_adress = driver.find_element(By.XPATH, PERM_ADDR_FIELD)
    submit = driver.find_element(By.XPATH, SUBMIT_BUTTON)

    name.send_keys("Alex")
    email.send_keys('mymail@gmail.com')
    current_adress.send_keys("Kharkiv, Shevchenka")
    permanent_adress.send_keys("Rivne, Shevchenka")
    submit.click()


