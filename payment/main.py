from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel
from starlette.requests import Request
import requests
import time

# FastAPI app
app = FastAPI()

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins = ['http://localhost:3000'],
    allow_methods = ['*'],
    allow_headers = ['*'],
)

# This should be a different database. Each MS needs their own database.
# But since I don't want to pay for a second database, let's pretend it is a second database.
redis = get_redis_connection(
    host = "redis-10848.c293.eu-central-1-1.ec2.cloud.redislabs.com",
    port = 10848,
    password = "fvwGXiItxmqhFCR9qA0Dth0CUQBkpvaa",
    decode_responses = True
)

class Order(HashModel):
    product_id: str
    price: float
    fee: float # the MS will buy the product but it will also add a fee
    total: float
    quantity: int # quantity that user will buy
    status: str # can be pending, completed or refunded

    class Meta:
        database = redis

@app.post('/orders')
async def create(request: Request): # this will send just ID and quantity. from the ID it will get the product
    body = await request.json()

    req = requests.get('http://localhost:8000/products/%s' % body['id'])
    product = req.json()

    order = Order(
        product_id = body['id'],
        price = product['price'],
        fee = 0.2 * product['price'],
        total = 1.2 * product['price'],
        quantity = body['quantity'],
        status = 'pending'
    )

    order.save()

    order_completed(order)

    return order

def order_completed(order: Order):
    time.sleep(5)
    order.status = 'completed'
    order.save()