from requests import get, post
from main import User, Product

print("Here is a list of routes: ")
routes_list = ['/', '/home', '/about', '/find-product', '/search', '/login', '/signup', '/product', '/add-product', '/rating', '/add-rating']

for i in routes_list:
    print(i)

user_route = input('Enter a route: ')
URL = 'http://localhost:8080'

while user_route != 'quit' and user_route in routes_list:
    match user_route:
        case '/':
            print(get(URL + user_route).json())
        case '/home':
            print(get(URL + user_route).json())
        case '/about':
            print(get(URL + user_route).json())
        case '/find-product':
            name = input('Enter the name of the product: ')
            price = input('Enter the price of the product: ')
            print(get('/'.join([URL, user_route, name, price])).json())
        case '/search':
            email = input('Enter an email address: ')
            print(get('/'.join([URL, user_route, email])).json())
        case '/login':
            email = input('Enter an email address: ')
            password = input('Enter the password: ')
            print(get('/'.join([URL, user_route]), params={'email': email, 'password': password}).json())
        case '/signup':
            first_name = input("Enter a first name: ")
            last_name = input("Enter a last name: ")
            email = input("Enter an email address: ")
            password = input("Enter a password: ")
            new_user = User(first_name=first_name, last_name=last_name, email=email, password=password)
            print(post('/'.join([URL, user_route]), data={'user': new_user}).json())
        case '/product':
            name = input('Enter the product name: ')
            price = int(input('Enter the product price: '))
            exp_date = input('Enter the expiration date: ')
            rating = input('Enter the product rating: ')
            product = Product(name=name, price=price, exp_date=exp_date, rating=rating)
            print(post('/'.join([URL, user_route]), data={'product': product}).json())
        case '/add-product':
            name = input('Enter the product name: ')
            price = int(input('Enter the product price: '))
            exp_date = input('Enter the expiration date: ')
            rating = input('Enter the product rating: ')
            product = Product(name=name, price=price, exp_date=exp_date, rating=rating)
            print(post('/'.join([URL, user_route]), data={'product': product}).json())
        case '/rating':
            product_name = input("Enter the product name: ")
            print(get('/'.join([URL, user_route, product_name])).json())
        case '/add-rating':
            product_name = input('Enter the product name: ')
            rating = input('Enter the product rating: ')
            print(get('/'.join([URL, user_route, product_name, rating])).json())
        case 'quit':
            print("Exiting...")
            break
    user_route = input('Enter a route or type "quit": ')

