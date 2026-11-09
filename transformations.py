

from decimal import Decimal, InvalidOperation
from models import Customer, Order

def normalize_orders(orders: list[dict]) -> tuple[list[Order], list[dict]]:
    clean_orders = []
    invalid_orders = []
    for order in orders:
        try:
            amount = Decimal(order["amount"].strip().replace(",", "."))
        except InvalidOperation as exc:
            invalid_orders.append({
                **order,
                "reason": f"amount is invalid: {order["amount"]!r}"
            })
            continue
        clean_order = {
            "order_id": int(order["order_id"]),
            "customer_id": int(order["customer_id"]),
            "amount": amount,
            "status": order["status"]
        }
        clean_orders.append(clean_order)
    return build_orders_objects(clean_orders), invalid_orders

def build_orders_objects(order_dicts: list[dict]) -> list[Order]:
    orders_obj_list = []
    for order in order_dicts:
        order_obj = Order(order["order_id"], order["customer_id"], order["amount"], order["status"])
        orders_obj_list.append(order_obj)
    return orders_obj_list

def normalize_customers(customers: list[dict]) -> tuple[list[Customer], list[dict]]:
    clean_customers = []
    invalid_customers = []
    for customer in customers:
        try:
            customer_id = int(customer["customer_id"])
            if customer["name"] is None or customer["name"].strip() == "":
                raise ValueError("name cant be None or empty")
            else:
                name = customer["name"]
        except ValueError as exc:
            invalid_customers.append({
                **customer,
                "reason": exc
            })
        country = customer.get("country", "UNKNOWN")
        if country is None or country.strip() == "":
            country = "UNKNOWN"
        email = customer.get("email", "missing_email")
        if email is None or email == "":
            email = "missing_email"
        clean_customer = {
            "customer_id": customer_id,
            "name": name,
            "country": country,
            "email": email
        }
        clean_customers.append(clean_customer)
    return build_customers_objects(clean_customers), invalid_customers

def build_customers_objects(customer_dicts: list[dict]) -> list[Customer]:
    customers_obj_list = []
    for customer in customer_dicts:
        customer_obj = Customer(customer["customer_id"], customer["name"], customer["country"], customer["email"])
        customers_obj_list.append(customer_obj)
    return customers_obj_list



