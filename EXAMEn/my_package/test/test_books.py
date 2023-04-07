import pytest
from EXAMEn.my_package.page import BookPage
import requests

@pytest.mark.usefixtures('chrome')
class TestBookStore:
    AUTHORS = ['Kyle Simpson', 'Marijn Haverbeke']
    PUBLISHERS = ["O\'Reilly Media", "No Starch Press"]
    TITLES = ['Git',"JavaScript", "Bullshit"]

    @classmethod
    def initialize_page(cls):
        driver = cls.driver
        cls.store = BookPage.BookPage(driver=driver)

    @pytest.fixture(autouse=True)
    def init_driver(self):
        yield self.initialize_page()

    def test_name_of_book_by_author(self):
        self.store.open()
        self.store.do_search("Richard")
        print(self.store.list_titles())
        assert self.store.get_title() in self.store.list_titles()

    @pytest.mark.parametrize("publisher",PUBLISHERS)
    def test_list_by_publisher(self,publisher):
        self.store.open()
        self.store.do_search(publisher)
        print(self.store.list_titles())
        if publisher == "No Starch Press":
            assert len(self.store.list_titles()) == 2
        else:
            assert len(self.store.list_titles()) == 6

    @pytest.mark.parametrize("authors", AUTHORS)
    def test_image_load(self,authors):
        self.store.open()
        self.store.do_search(authors)
        responce = requests.get(self.store.get_image_sources())
        status_code = responce.status_code
        assert status_code == 200

    @pytest.mark.parametrize("titles", TITLES,)
    def test_search(self,titles):
        self.store.open()
        self.store.do_search(titles)
        print(self.store.list_titles())
        if titles == "Git":
            assert len(self.store.list_titles()) == 1
        if titles == "JavaScript":
            assert len(self.store.list_titles()) == 4
        if titles == "Bullshit":
            assert len(self.store.list_titles()) == 0

    def test_sort_by_publisher(self):
        self.store.open()
        self.store.list_titles()
        self.store.first_row_publisher()
        print(f'first row was : {self.store.first_row_publisher()}')
        self.store.sort_by_pyblisher()
        assert self.store.first_row_publisher() == self.PUBLISHERS[1]
        print(f'Now first row is : {self.store.first_row_publisher()}')
        self.store.sort_by_pyblisher()
        self.store.first_row_publisher()
        assert self.store.first_row_publisher() == self.PUBLISHERS[0]
        print(f'Now first row is: {self.store.first_row_publisher()}')

