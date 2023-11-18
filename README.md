# Payment App

## Tech Stack
- Language: Python
- Framework: Fast API
- Database: PostgreSQL
- ORM: Peewee ORM

   
## Database Design : 
<img width="1027" alt="image" src="https://github.com/gulshantelkar/Payment-App/assets/99161604/38e96ebe-1505-4730-b769-780664f1d427">


## Running the System

1. Activate the env ```source venv/bin/activate```
2. if first step fails run this command ```python3 -m venv venv ```
3. then try step 1
4. Install the requirements ```pip install -r requirements.txt```

5. Run the Command: ``` uvicorn uvicorn_conf:app --reload  ```

6. Open Postman and test the endpoints

### To enable authorization, you need to assign a token to each user and explicitly assign the admin role to at least one user.
### And put in the header section

## Create Users

- Endpoint: `http://127.0.0.1:8000/users/`
- <img width="1006" alt="image" src="https://github.com/gulshantelkar/Payment-App/assets/99161604/f3860e97-2a15-4fbb-bbf3-9b4b120e1fdd">


## Login 

- Endpoint: `http://127.0.0.1:8000/login`
- <img width="1031" alt="image" src="https://github.com/gulshantelkar/Payment-App/assets/99161604/8e71f3ef-49b1-4be3-846e-59764f957664">


## Get user by id ( Admin +  user id)

- Endpoint: `http://127.0.0.1:8000/users/8653ca46-5b4b-4b29-8c22-91ddd5c4e77c`
- <img width="1030" alt="image" src="https://github.com/gulshantelkar/Payment-App/assets/99161604/70945108-e58f-4e85-b692-e6b501a8c99b">


## List all Users( Admin Only)

- Endpoint: `http://127.0.0.1:8000/users`
- <img width="1009" alt="image" src="https://github.com/gulshantelkar/Payment-App/assets/99161604/08d20b19-2228-431c-af99-e7795d4b6a7e">


## Create Invoices( Admin Only)

- Endpoint: `http://127.0.0.1:8000/invoices`
- <img width="1031" alt="image" src="https://github.com/gulshantelkar/Payment-App/assets/99161604/fe67a636-2f50-4c3a-9cd7-cc50a74bb3a2">


## Get invoice by id( Admin + receiver + payer)

- Endpoint: `http://127.0.0.1:8000/invoices/5e7e7447-f94e-460e-89cf-fa9c4b161a8d`
- <img width="1006" alt="image" src="https://github.com/gulshantelkar/Payment-App/assets/99161604/a5e77c3c-4bab-4636-8ba6-22802f78b5c8">


## List all Invoices( Admin only)

- Endpoint: `http://127.0.0.1:8000/invoices`
- <img width="1031" alt="image" src="https://github.com/gulshantelkar/Payment-App/assets/99161604/3ab87f77-a7ad-4ba9-83bd-dc93664b3742">


## Create Invoice Transaction (Admin Only)

- Endpoint: `http://127.0.0.1:8000/invoice-transactions`
- <img width="1016" alt="image" src="https://github.com/gulshantelkar/Payment-App/assets/99161604/f5762f1f-9806-4ec5-ac3b-297ee7696928">

## Get Invoice Transaction by Invoice id(Admin Only)

- Endpoint: `http://127.0.0.1:8000/invoice-transactions/invoice/5e7e7447-f94e-460e-89cf-fa9c4b161a8d`
- <img width="1029" alt="image" src="https://github.com/gulshantelkar/Payment-App/assets/99161604/4e07972b-06de-4ca0-9b2d-29273c8d8d2a">

## Delete Invoice by Invoice id(Admin Only)

- Endpoint: `http://127.0.0.1:8000/invoices/5e7e7447-f94e-460e-89cf-fa9c4b161a8d`
- <img width="1015" alt="image" src="https://github.com/gulshantelkar/Payment-App/assets/99161604/8c7f553a-92e6-4e7f-962c-2787a5bed719">

## Update Invoice by Invoice id(Admin Only)

- Endpoint: `http://127.0.0.1:8000/invoices/5e7e7447-f94e-460e-89cf-fa9c4b161a8d`
- ![image](https://github.com/gulshantelkar/Payment-App/assets/99161604/10ac5710-ae4c-4d46-b08a-6d97bed2895b)


## Webhook for Payment success

- Endpoint: `http://localhost:8000/webhooks/payment/success`
- <img width="1011" alt="image" src="https://github.com/gulshantelkar/Payment-App/assets/99161604/51e93b03-561e-448b-a017-dd1470032c35">


## Webhook for Payment failure

- Endpoint: `http://localhost:8000/webhooks/payment/failure`
- <img width="997" alt="image" src="https://github.com/gulshantelkar/Payment-App/assets/99161604/94fa7e4b-f6ff-40a8-9218-dc11526262d7">


## Webhook for Payment Refund

- Endpoint: `http://localhost:8000/webhooks/refund`
- <img width="1020" alt="image" src="https://github.com/gulshantelkar/Payment-App/assets/99161604/24e61623-ef3c-4417-ac8c-af53c32dc3b2">



