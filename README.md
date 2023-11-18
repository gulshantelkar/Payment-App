# Payment App

## Tech Stack
- Language: Python
- Framework: Fast API
- Database: PostgreSQL
- ORM: Peewee ORM

   
## Database Design : 
<img width="1027" alt="image" src="https://github.com/gulshantelkar/Payment-App/assets/99161604/38e96ebe-1505-4730-b769-780664f1d427">


## Running the System

1. Activate the env ```source venv/bin/activate```.

2. Run the Command: ``` uvicorn uvicorn_conf:app --reload  ```

3. Open Postman and test the endpoints

   
## Create Users

- Endpoint: `http://127.0.0.1:8000/users/`
- <img width="1006" alt="image" src="https://github.com/gulshantelkar/Payment-App/assets/99161604/f3860e97-2a15-4fbb-bbf3-9b4b120e1fdd">


## Login 

- Endpoint: `http://127.0.0.1:8000/login`
- <img width="1031" alt="image" src="https://github.com/gulshantelkar/Payment-App/assets/99161604/8e71f3ef-49b1-4be3-846e-59764f957664">


## Get user by id (admin + that user)

- Endpoint: `http://127.0.0.1:8000/users/8653ca46-5b4b-4b29-8c22-91ddd5c4e77c`
- <img width="1030" alt="image" src="https://github.com/gulshantelkar/Payment-App/assets/99161604/70945108-e58f-4e85-b692-e6b501a8c99b">


## List all Users( Admin Only)

- Endpoint: `http://127.0.0.1:8000/users`
- <img width="1009" alt="image" src="https://github.com/gulshantelkar/Payment-App/assets/99161604/08d20b19-2228-431c-af99-e7795d4b6a7e">


## Create Invoices( Admi Only)

- Endpoint: `http://127.0.0.1:8000/invoices`
- <img width="1031" alt="image" src="https://github.com/gulshantelkar/Payment-App/assets/99161604/fe67a636-2f50-4c3a-9cd7-cc50a74bb3a2">


## List of All Orders Endpoint

- Endpoint: `http://localhost:8000/pizza-ordering/api/orders/`
- ![Image](https://github.com/gulshantelkar/Pizza-System/assets/99161604/32882baf-d236-408e-996d-9e6a4a238bfc)

## List of All Pizzas

- Endpoint: `http://localhost:8000/pizza-ordering/api/pizzas/`
- ![Image](https://github.com/gulshantelkar/Pizza-System/assets/99161604/582c3447-c8e4-4052-aba3-efa90620456e)

## Get a Single Entry of an Order

- Endpoint: `http://localhost:8000/pizza-ordering/api/order/id`
- ![Image](https://github.com/gulshantelkar/Pizza-System/assets/99161604/a46fc478-9c81-4d42-8493-109fa94f1242)

# I have also added Unit Testing for the API's 

1. Open new terminal : ``` cd pizza_delivery ```
2. Run this Commabd: ```python manage.py test pizza_ordering.tests```

## Get a Single Entry of Pizza Base, Cheese, Topping, Pizza

- Endpoints:
- `http://localhost:8000/pizza-ordering/api/pizza_base/id`
- `http://localhost:8000/pizza-ordering/api/cheese/id`
- `http://localhost:8000/pizza-ordering/api/topping/id`
- `http://localhost:8000/pizza-ordering/api/pizza/id`
- `http://localhost:8000/pizza-ordering/api/topping/id`
