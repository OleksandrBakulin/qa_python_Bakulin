import pytest


class TestFirst:


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

