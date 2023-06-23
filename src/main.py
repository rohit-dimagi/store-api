from typing import List

from fastapi import FastAPI, Query, status
from loguru import logger

import models
from database import SessionLocal
from utils import Item, SanitizeQueryParam

logger.info("staring app server..")
app = FastAPI()
db = SessionLocal()


@app.get("/ready", status_code=status.HTTP_200_OK)
def readiness():
    return {"ready": "true"}


@app.get(
    "/get/messages/{account_id}",
    response_model=List[Item],
    status_code=status.HTTP_200_OK,
)
def get_all_msg(account_id: str):
    logger.info(f"Getting all the msg for Account ID: {account_id}")
    items = db.query(models.Item).filter(models.Item.account_id == account_id).all()
    return items


@app.get("/search", response_model=List[Item], status_code=status.HTTP_200_OK)
def search_messages(
    message_id: str = Query(None, description="Comma-separated message IDs"),
    sender_number: str = Query(None, description="Comma-separated sender numbers"),
    receiver_number: str = Query(None, description="Comma-separated receiver numbers"),
):
    if message_id:
        message_id = SanitizeQueryParam().sanitize_input(message_id)
        logger.info(f"Searching messages record for message ID: {message_id}")
        items = (
            db.query(models.Item).filter(models.Item.message_id.in_(message_id)).all()
        )
        return items

    if sender_number:
        sender_number = SanitizeQueryParam().sanitize_input(sender_number)
        logger.info(f"Searching messages records from Sender Number: {sender_number}")
        items = (
            db.query(models.Item)
            .filter(models.Item.sender_number.in_(sender_number))
            .all()
        )
        return items

    if receiver_number:
        receiver_number = SanitizeQueryParam().sanitize_input(receiver_number)
        logger.info(f"Searching messages records to Reciever Number: {receiver_number}")
        items = (
            db.query(models.Item)
            .filter(models.Item.receiver_number.in_(receiver_number))
            .all()
        )
        return items


@app.post("/create", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    new_item = models.Item(
        account_id=item.account_id,
        message_id=item.message_id,
        receiver_number=item.receiver_number,
        sender_number=item.sender_number,
    )
    logger.info(f"Creating a new Msg record for Account ID: {item.account_id}")
    db.add(new_item)
    db.commit()

    return new_item
