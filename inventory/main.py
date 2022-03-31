from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel

# FastAPI app
app = FastAPI()

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins = ['http://localhost:3000'],
    allow_methods = ['*'],
    allow_headers = ['*'],
)

# Connection to redis
redis = get_redis_connection(
    host = "redis-10848.c293.eu-central-1-1.ec2.cloud.redislabs.com",
    port = 10848,
    password = "fvwGXiItxmqhFCR9qA0Dth0CUQBkpvaa",
    decode_responses = True
)

# Table that defines a product
class Product(HashModel):
    name: str
    price: float
    quantity: int

    # To make the product connected to the Redis DB, a new Meta class is defined
    class Meta:
        database = redis

@app.get('/products')
def return_all_products_in_inventory():
    return [format(pk) for pk in Product.all_pks()]

def format(pk: str):
    product = Product.get(pk)
    return {
        'id': product.pk,
        'name': product.name,
        'price': product.price,
        'quantity': product.quantity
    }

@app.post('/products')
def create_product(product: Product):
    return product.save()

@app.get('/products/{pk}')
def return_single_product(pk: str):
    return Product.get(pk)

@app.delete('/products/{pk}')
def delete(pk: str):
    return Product.delete(pk)
