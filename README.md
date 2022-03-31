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

What needs to be done:

- Internal HTTP requests
- Background tasks
- Redis streams implementation
- React Frontend implementation

## Notes for myself

### How to run Inventory MS

    uvicorn main:app --reload