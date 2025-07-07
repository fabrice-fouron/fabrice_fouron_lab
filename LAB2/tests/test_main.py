from requests import get, post
import unittest
from main import User, Product
import json

class testLAB(unittest.TestCase): 
    def test_root(self):
        url = 'http://localhost:8080/'
        response = get(url)
        self.assertEqual(200, response.status_code)

    def test_home(self):
        url = 'http://localhost:8080/home'
        response = get(url)
        self.assertEqual(200, response.status_code)

    def test_about(self):
        url = 'http://localhost:8080/about'
        response = get(url)
        self.assertEqual(200, response.status_code)

    def test_find_product(self):
        url = 'http://localhost:8080/find-product'
        name = 'Apple'
        price = 5
        response = get(url + f'/{name}/{str(price)}')
        self.assertEqual(200, response.status_code)

    def test_search(self):
        url = 'http://localhost:8080/search'
        email = 'fouronf@wit.edu'
        response = get(url + f'/{email}')
        self.assertEqual(200, response.status_code)

    def test_login(self):
        url = 'http://localhost:8080/login'
        parameters = {"email": "fouronf@wit.edu", "password": "helloworld"}
        response = get(url, params=parameters)
        self.assertEqual(200, response.status_code)

    def test_signup(self):
        url = 'http://localhost:8080/signup'
        parameters = {
            "email": "fouronf@wit.edu", 
            "password": "helloworld"
        }
        user = User(
            first_name="John",
            last_name="Doe",
            email='jdoe@gmail.com',
            password='1234'
        )
        response = post(url, data=user.model_dump_json())
        self.assertEqual(200, response.status_code)

    def test_display_product_info(self):
        url = 'http://localhost:8080/product'
        product = Product(
            name="Apple", 
            price=5, 
            exp_date="2025/04/12", 
            rating=7
        )
        response = post(url, data=product.model_dump_json())
        self.assertEqual(200, response.status_code)

    def test_add_product(self):
        url = 'http://localhost:8080/add-product'
        product = Product(
            name="Apple", 
            price=5, 
            exp_date="2025/04/12",
            rating=0
        )
        response = post(url, data=product.model_dump_json())
        self.assertEqual(200, response.status_code)

    def test_rating(self):
        product_name = "Apple"
        url = f'http://localhost:8080/rating/{product_name}'
        response = get(url)
        self.assertEqual(200, response.status_code)

    def test_add_rating(self):
        product_name = "Apple"
        rating = 5
        url = f'http://localhost:8080/add-rating/{product_name}/{rating}'
        response = get(url)
        self.assertEqual(200, response.status_code)

    def test_headers(self):
        email = "fouronf@wit.edu"
        username = "mr elephant"
        url = "http://localhost:8080/headers"
        response = get(url, headers={"email": email, "username": username})
        print("HEADERS: ", response.content)
        self.assertEqual(200, response.status_code)

    def test_cookie(self):
        random_name = "superman"
        url = "http://localhost:8080/cookie"
        response = get(url, cookies={"random_name": random_name})
        print("COOKIE: ", response.content)
        self.assertEqual(200, response.status_code)