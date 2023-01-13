import pytest


@pytest.fixture(scope="function")
def third_fixture():
    print('\nThe beginning of the fixture execution')
    yield
    print('\nThe end of the fixture execution')