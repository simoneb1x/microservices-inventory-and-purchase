from main import redis, Order
import time

key = 'refund_order'
group = 'payment-group'

# Redis Consumer group
try:
    redis.xgroup_create(key, group)
except:
    print('Group already exists.')

# Consuming the messages
# It gets the event through Redis Streams, the results are looped. The order is got, the product is got and the quantity is reduced.
while True:
    try:
        results = redis.xreadgroup(group, key, {key: '>'}, None)

        if results != []:
            for result in results:
                obj = result[1][0][1]
                order = Order.get(obj['pk'])
                order.status = 'refunded'
                order.save()

    except Exception as exc:
        print(str(exc))

    time.sleep(1)