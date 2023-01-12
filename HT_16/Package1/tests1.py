import pytest


@pytest.fixture(scope="function", autouse=True)
def func_fixture():
    print('\nThe beginning of the fixture execution')
    yield
    print('\nThe end of the fixture execution')

class FirstTest:


    @pytest.mark.from_class
    def test_one(self):
        print("\nfirst test execution")
        pass

    @pytest.mark.from_class
    def test_two(self):
        print("\nsecond test execution")
        pass

    @pytest.mark.from_class
    def test_third(self):
        print("\nthird test exrcution")
        pass

    @pytest.mark.from_class
    def test_fourth(self):
        print("\nfourth test execution")
        pass

    @pytest.mark.from_class
    def test_fifth(self):
        print("\nfifth test exrcution")
        pass

@pytest.mark.from_class
def test_fifth():
    print("\nfifth test exrcution")
    pass