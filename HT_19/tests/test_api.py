'''API tests: Створити по одному синтетичному API тесту, для кожної функції CRUD (Create, read, update, delete).
Створити кілька реальних API тестів на https://reqres.in/: отримати методом GET кілька користувачів,
отримати методом GET одного користувача, пройти авторизацію за допомогою метода GET, створити персону з допомогою метода POST'''

import json
import requests

class TestSynctetic():
    def test_create(self):
        url = "https://reqres.in/api/users"
        data = {
            "name": "John Doe",
            "job": "Software Engineer"
        }
        response = requests.post(url, data=data)
        assert response.status_code == 201
        assert response.json()["name"] == "John Doe"
        assert response.json()["job"] == "Software Engineer"
        assert "id" in response.json()

    def test_read(self):
        url = "https://reqres.in/api/users/2"
        response = requests.get(url)
        assert response.status_code == 200
        assert response.json()["data"]["id"] == 2
        assert response.json()["data"]["email"] == "janet.weaver@reqres.in"

    def test_update(self):
        url = "https://reqres.in/api/users/2"
        data = {
            "name": "Janet Doe",
            "job": "Software Developer"
        }
        response = requests.put(url, data=data)
        assert response.status_code == 200
        assert response.json()["name"] == "Janet Doe"
        assert response.json()["job"] == "Software Developer"

    def test_delete_user(self):
        url = "https://reqres.in/api/users/2"
        response = requests.delete(url)
        assert response.status_code == 204


class TestApi():
    def test_get_users(self):
        users_response = requests.get('https://reqres.in/api/users?page=2')
        assert users_response.status_code == 200
        data = json.loads(users_response.text)
        users = data['data'][:3]
        print(users)

    def test_get_single_user(self):
        s_user_response = requests.get('https://reqres.in/api/users/2')
        assert s_user_response.status_code == 200
        s_data = json.loads(s_user_response.text)
        user = s_data['data']
        print(user)

    def test_post_autorisation(self):
        autorisation= {"email": "eve.holt@reqres.in",
        "password" :"cityslicka"}
        url = 'https://reqres.in/api/login'
        autorisation_response = requests.post(url,autorisation)
        assert autorisation_response.status_code == 200
        assert "QpwL5tke4Pnpja7X4" in autorisation_response.text
        print(autorisation_response.text)

    def test_post_create(self):
        user = {
        "name": "morpheus",
        "job": "leader"}
        url = 'https://reqres.in/api/users'
        create_response = requests.post(url, user)
        assert create_response.status_code == 201
        print(create_response.text)

