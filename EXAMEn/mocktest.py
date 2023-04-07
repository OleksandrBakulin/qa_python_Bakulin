import pytest
from unittest.mock import Mock


class One:
    def some_test(self):
        return "this text to be printer first"

@pytest.fixture(scope="function",autouse=True)
def myfixture():
    yield One()

def test_mock_synt(myfixture,monkeypatch):
    print(f'{myfixture.some_test()}')
    monkeypatch.setattr(
        One,
        "some_test",
        Mock(return_value="new text is mocked"))
    print(f'{myfixture.some_test()}')

