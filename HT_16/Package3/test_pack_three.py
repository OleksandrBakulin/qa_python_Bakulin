import pytest


@pytest.mark.pack
@pytest.mark.joint
def test_one(third_fixture):
    print("\nfirst test execution")
    pass


@pytest.mark.pack
@pytest.mark.rest
def test_two(third_fixture):
    print("\nsecond test execution")
    pass


@pytest.mark.pack
@pytest.mark.rest
def test_third(third_fixture):
    print("\nthird test execution")
    pass


@pytest.mark.pack
@pytest.mark.joint
def test_fourth(third_fixture):
    print("\nfourth test execution")
    pass


@pytest.mark.pack
@pytest.mark.rest
def test_fifth(third_fixture):
    print("\nfifth test execution")
    pass

def test_six(third_fixture):
    print("\nsix test execution")
    pass