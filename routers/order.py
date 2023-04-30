from typing import List

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from starlette import status

from utils.enums import CriterionTypes
from utils.process_orders import process_orders

order = APIRouter()

order_list = [
    {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"},
    {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": "pending"},
    {"id": 3, "item": "Headphones", "quantity": 3, "price": 99.90, "status": "completed"},
    {"id": 4, "item": "Mouse", "quantity": 4, "price": 24.99, "status": "canceled"}
]


class Order(BaseModel):
    orders: List
    criterion: CriterionTypes


@order.post('/solution/', status_code=status.HTTP_200_OK)
async def solution(data: Order):
    for i in data.orders:
        if i.get('price') < 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"You should check that the price of an item {i.get('id')} can't be negative")
        if i.get('status') == "":
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"You should check that the status of an item {i.get('id')} can't be empty")

    get_process_orders = process_orders(order_list, data.criterion.value)

    return {'total_revenue': get_process_orders}
