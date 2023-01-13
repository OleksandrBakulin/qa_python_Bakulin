import pytest

@pytest.fixture(scope="class", autouse=True)
def func_fixture():
    print('\nThe beginning of the fixture execution')
    yield
    print('\nThe end of the fixture execution')