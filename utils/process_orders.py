from typing import List


def process_orders(orders: List, criterion: str) -> float:
    if criterion == "all":
        return round(sum(i.get('price') for i in orders), 2)
    return round(sum(i.get('price') if i.get('status') == criterion else 0 for i in orders))
