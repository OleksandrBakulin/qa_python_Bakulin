import pytest


@pytest.fixture(scope="module", autouse=True)
def second_fixture():
    print("\nFixture for this test start")
    yield
    print("\nFixture for this test ended")


metal_bands = ["Devourment", 'Archspire', 'Deicide', 'Asphyx', 'Nile']


@pytest.mark.param
@pytest.mark.parametrize('bands', ["Archspire", 'Nile', 'Grave'], ids=['band1', 'band2', 'band3'])
def test_par_one(bands):
    assert bands in metal_bands


@pytest.mark.param
@pytest.mark.parametrize('key, value', [(1, 1), ("local", "local"), (5.0, 5.0)], ids=["ints", "strings", "floats"])
def test_par_one(key, value):
    print(f"\n{key},{value}")



weak_passwords = ("qwerty", "123456", "54321", 'password', 'admin')
weak_login = ("admin", "user", "master")


@pytest.mark.param
@pytest.mark.parametrize('password, login', [('admin','1234')], ids=["user_creds"])
def test_ip(password,login):
    assert password in weak_passwords and login in weak_login
