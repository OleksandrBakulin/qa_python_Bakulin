import pytest


metal_bands = ["Devourment", 'Archspire', 'Deicide', 'Asphyx', 'Nile']


@pytest.mark.param
@pytest.mark.parametrize('bands', ["Archspire", 'Nile', 'Grave'])
def test_par_one(bands):
    assert bands in metal_bands


@pytest.mark.param
@pytest.mark.parametrize('key, value', [(1, 1), ("local", "local"), (5.0, 5.0)], ids=["ints", "strings", "floats"])
def test_par_two(key, value):
    assert key == value
    print(f"\n{key},{value}")



weak_passwords = ("qwerty", "123456", "54321", 'password', 'admin')
weak_login = ("admin", "user", "master")


@pytest.mark.param
@pytest.mark.parametrize(' login, password', [('admin','123456')], ids=["user_creds"])
def test_ip(login, password):
    assert password in weak_passwords and login in weak_login
