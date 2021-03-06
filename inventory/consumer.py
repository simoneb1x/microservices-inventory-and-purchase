from main import redis, Product
import time

key = 'order_completed'
group = 'inventory-group'

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
                
                try:
                    product = Product.get(obj['product_id'])
                    product.quantity -= int(obj['quantity'])
                    product.save()
                except:
                    redis.xadd('refund_order', obj, '*') 
                    
                    

    except Exception as exc:
        print(str(exc))

    time.sleep(1)