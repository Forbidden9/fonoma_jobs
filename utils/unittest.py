from routers.order import order_list
from utils.enums import CriterionTypes

# Bad List with negative price
test_bad_negative_order_list = [
    {"id": 1, "item": "Laptop", "quantity": 1, "price": -999.99, "status": "completed"}
]

# Bad List with status empty
test_bad_status_order_list = [
    {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": ""},
]

# JSON Encoded Data
data_bad_negative = {
    "orders": test_bad_negative_order_list,
    "criterion": CriterionTypes.completed
}

data_bad_status = {
    "orders": test_bad_status_order_list,
    "criterion": CriterionTypes.completed
}

data_ok = {
    "orders": order_list,
    "criterion": CriterionTypes.completed
}
