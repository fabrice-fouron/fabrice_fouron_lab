from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
users = {
    1: {
        "First Name": "John",
        "Last Name": "Doe",
        "Email": "jdoe@gmail.com",
        "Password": "helloworld",
        "money": 15
    }
}

products = {
    1: {
        "Product Name": "Apple",
        "Price": 2,
        "Expiration Date": "01/01/01",
        "Rating": 7.5,
        "Quantity": 9
    }
}

class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

class Product(BaseModel):
    name: str
    price: int
    exp_date: str
    rating: float

@app.get("/")
async def root():
    return "This is a simple route"

@app.get("/home")
async def home():
    return "This project attempts to simulate managers and inventory of their store and customers as well"

@app.get("/about")
async def about():
    return {"message": "This is content for that talks about the main purpose of this project."}

@app.get("/find-product/{name}/{price}")
async def find_product(name: str, price: int):
    for i in products.keys():
        if products[i]["Product Name"] == name:
            return products[i] # information about the product
    return "Product not found"

@app.get("/search/{email}")
async def search(email: str):
    for i in users.keys():
        temp = users[i]
        if temp["Email"] == email:
            return "User found"
    return "User not found"

@app.get("/login")
async def login(email: str, password: str):
    '''The user can login'''
    for i in users.keys():
        temp = users[i]
        if (await search(email)) == "User found" and password == temp["Password"]:
            return "Logged In"
    return "User not found"

@app.post("/signup")
async def signup(user: User):
    '''The user can sign up'''
    try:
        users[len(users.keys()) + 1] = {
            "First Name": user.first_name,
            "Last Name": user.last_name,
            "Email": user.email
        }
        return users

    except Exception as e:
        return e

@app.post("/product")
async def buy(product: Product):
    if product.name == None:
        return "This page displays the different products that are available"
    else:
        return f"This product is a(n) {product.name} and its price is ${product.price}"

@app.post("/add-product")
async def get_price(product: Product):
    if len(product.name) > 0:
        products[len(products.keys()) + 1] = {
            "Product Name": product.name,
            "Price": product.price,
            "Expiration Date": product.exp_date,
            "Rating": 0
        }
        return f"The new product '{product.name}' was added!\n{products}"
    else:
        return "Provide the required information"

@app.get("/rating/{product_name}")
async def get_reviews(product_name: str):
    if len(product_name) > 0:
        for i in products.keys():
            if products[i]["Product Name"] == product_name:
                return f"The rating of the {product_name} is {products[i]['Rating']}"
    return "No products match the provided name"

@app.get("/add-rating/{product_name}/{rating}")
async def add_rating(product_name: str, rating: int):
    if len(product_name) > 0:
        for i in products.keys():
            if products[i]["Product Name"] == product_name:
                if products[i]["Rating"] == 0:
                    products[i]["Rating"] = rating
                else:
                    products[i]["Rating"] = (products[i]["Rating"] + rating) / 2
                return f"The new rating of the {product_name} is {products[i]['Rating']}" 
    return "The product name does not match any of what already exists."
