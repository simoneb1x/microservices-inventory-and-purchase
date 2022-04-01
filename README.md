# Microservices Store mockup

This is a mockup of a store that is based on microservices architecture.

## Architecture

The architecture involves:

- A Front-End based on React;
- Two FastAPI microservices:
    - an Inventory MS,
    - a Payment MS;
- A single Redis DB for both microservices (I know it would take two databases, but for the purposes of the mockup I will only use one);
- A Redis Stream, equivalent to a single partition of a Kafka topic

This is still WIP (last commit: 01/04/22).

## Roadmap

What I did:

- Inventory MS implementation
- Redis DB initialization
- Products CRUD in inventory
- Payment MS implementation
- Internal HTTP requests
- Background tasks
- Redis Streams implementation
- Two consumers for both MS

What needs to be done:

- React Frontend implementation

## Notes for myself

At the moment the project only starts locally. Deployment on the Internet should be foreseen.

### How to run microservices

    uvicorn main:app --reload

### How to run Redis Streams consumers 

Make sure to be in the correct directory, then:

    python3 consumer.py

### How to run Front-End

    npm start

### How Redis Streams works in this project

1. An event is sent to Redis Streams
2. When the order is completed, the status of the order is changed
3. In the meanwhile, a consumer will wait for the order_completed event
4. An event is sent to Redis Streams with a key (like, 'order_completed')