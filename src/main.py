from fastapi import FastAPI, status, Query
from pydantic import BaseModel, constr, Field
from typing import List
from uuid import UUID, uuid4
from database import SessionLocal
import models
from utils import PhoneNumber
from utils import SanitizeQueryParam

app = FastAPI()

class Item(BaseModel):
    account_id:constr(regex=r'^[a-zA-Z0-9]+$')
    message_id: UUID = Field(default_factory=uuid4)
    sender_number: PhoneNumber
    receiver_number: PhoneNumber

    class Config:
        orm_mode=True

db = SessionLocal()

@app.get('/get/messages/{account_id}', response_model=List[Item], status_code=status.HTTP_200_OK)
def get_all_msg(account_id:str):
    items=db.query(models.Item).filter(models.Item.account_id==account_id).all()
    return items




@app.get('/search', response_model=List[Item], status_code=status.HTTP_200_OK)
def search_messages(
    message_id: str = Query(None, description="Comma-separated message IDs"),
    sender_number: str = Query(None, description="Comma-separated sender numbers"),
    receiver_number: str = Query(None, description="Comma-separated receiver numbers")
):
    if message_id:
        if "," in message_id:
            message_id=message_id.strip('"').split(",")
        else:
            message_id=[message_id.strip('"')]
        items=db.query(models.Item).filter(models.Item.message_id.in_(message_id)).all()
        return items
    
    if sender_number:
        if "," in sender_number:
            sender_number=sender_number.strip('"').split(",")
        else:
            sender_number=[sender_number.strip('"')]
        items=db.query(models.Item).filter(models.Item.sender_number.in_(sender_number)).all()
        return items
    

    if receiver_number:
        if "," in receiver_number:
            receiver_number=receiver_number.strip('"').split(",")
        else:
            receiver_number=[receiver_number.strip('"')]
        items=db.query(models.Item).filter(models.Item.receiver_number.in_(receiver_number)).all()
        return items
    


@app.post('/create', response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item:Item):
    new_item=models.Item(
        account_id=item.account_id,
        message_id=item.message_id,
        receiver_number=item.receiver_number,
        sender_number=item.sender_number
    )
    db.add(new_item)
    db.commit()

    return new_item