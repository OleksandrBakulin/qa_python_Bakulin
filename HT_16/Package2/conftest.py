import pytest


@pytest.fixture(scope="function", autouse=True)
def second_fixture():
    print("\nFixture for this test start")
    yield
    print("\nFixture for this test ended")
