# store-api
This is a Sample REST Api writen in python using FastAPI and Postgres 
## Local Development
1. Create a Python virtual Environment
1. Install requirements
1. export DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
1. start the app server

```
$ python -m venv ~/.store-api
$ source ~/.store-api/bin/activate
$ pip install -r requirements.txt
$ cd src ; uvicorn main:app --reload
```
Goto http://localhost:8000/docs

## Routes:
1. `/get/messages/<account-id>` : returns list of messages of the mentioned account-id
1. `/create`: Create a new message records with this schema
    ```
        {
        “account_id”: “<id>”
        “message_id”: “<random-uuid>”,
        “sender_number”: “<PHONE_NUMBER>”,
        “receiver_number”: “<PHONE_NUMBER>”
        }
    ```
1. `/search`: Search records using different filters -> `/search?message_id=”1,2”` , `/search?sender_number=”1,2”`, `/search?receiver_number=”1,2”`


## Pipeline
It contains a jenkins pipeline which is triggered with Github webhook and Build and push docker image to ECR.
