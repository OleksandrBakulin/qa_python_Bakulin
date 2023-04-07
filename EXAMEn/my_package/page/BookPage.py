from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BookPage:
    URL = 'https://demoqa.com/books'

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.__store_name_loc = (By.CLASS_NAME, 'main-header')
        self.__search_field_loc = (By.ID, 'searchBox')
        self.__book_list_body_loc = (By.CLASS_NAME, 'rt-tbody')
        self.__header_bar_loc = (By.CLASS_NAME, 'rt-tr')
        self.__headers_loc = (
            By.XPATH, '//div[@class="rt-tr"]'
                      '//div[contains(@class, "content")]')
        self.__books_loc = (
            By.XPATH,
            '//div[@role="row"][not(contains(@class, "pad"))]'
            '[contains(@class, "odd") or contains(@class, "even")]')
        self.__title_loc = (By.XPATH, '//span[contains(@id, "see-book")]')
        self.__image_loc = (By.XPATH, '//img[contains(@src,"/images/bookimage")]')
        self.__publisher_sort = (By.XPATH, '//div[contains(@class, "rt-tr -odd")]//div[contains(@class, "rt-td")]')
    def open(self):
        self.driver.get(url=self.URL)
        return self

    def get_name(self) -> str:
        return self.driver.find_element(*self.__store_name_loc).text
    def wait_for_visible(self, locator, timeout: int = 10):
        WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_element_located(locator))

    def _get_element_locator_by_header_name(self, header):
        column_index = self.get_headers().index(header)
        raw_locator = self.__books._locator._description
        locator = f"//{''.join(raw_locator.split('//')[1::])[:-3:]}" \
                  f"/div[{column_index + 1}]"
        return locator

    def get_headers(self):
        locator = self.__headers_loc
        self.wait_for_visible(locator)
        return [
            header.text
            for header in self.driver.find_elements(*locator)
            if len(header.text) > 0]

    def get_header_button(self, name):
        locator = self.__headers_loc
        self.wait_for_visible(locator)
        return [header for header in self.driver.find_elements(*locator)
                if header.text == name][0]

    def do_search(self, search_string: str):
        locator = self.__search_field_loc
        self.driver.find_element(*locator).send_keys(search_string)

    def get_title(self):
        locator = self.__title_loc
        title = self.driver.find_element(*locator).text
        return title

    def list_titles(self):
        locator = self.__title_loc
        titles_list = []
        titles = self.driver.find_elements(*locator)
        for i in titles:
           titles_list.append(i.text)
        return titles_list

    def get_image_sources(self):
        locator = self.__image_loc
        img = self.driver.find_element(*locator)
        img_src = img.get_attribute('src')
        return img_src

    def sort_by_pyblisher(self):
        locator = self.__headers_loc
        button = self.driver.find_elements(*locator)[3]
        button.click()

    def first_row_publisher(self):
        locator = self.__publisher_sort
        check = self.driver.find_elements(*locator)[3]
        return check.text




