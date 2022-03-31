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
    quantity_available: int

    # To make the product connected to the Redis DB, a new Meta class is defined
    class Meta:
        database = redis

@app.get('/products')
def return_all_keyproducts_in_inventory():
    return Product.all_pks()

@app.post('/products')
def create(product: Product):
    return product.save()