

from decimal import Decimal

class Customer:
    def __init__(self, customer_id: int, name: str, country: str, email: str) -> None:
        if type(customer_id) is not int:
            raise TypeError("customer_id must be int")
        if not isinstance(name, str):
            raise TypeError("name must be text")
        if name.strip() == "":
            raise ValueError("name cant be empty")
        if not isinstance(country, str):
            raise TypeError("country must be text")
        if country.strip() == "":
            raise ValueError("country cant be empty")
        if not isinstance(email, str):
            raise TypeError("email must be text")
        if email.strip() == "":
            raise ValueError("email cant be empty")
        self.customer_id = customer_id
        self.name = name.strip().capitalize()
        self.country = country.strip().upper()
        self.email = email.strip().lower()

class Order:
    def __init__(self, order_id: int, customer_id: int, amount: Decimal, status: str) -> None:
        if type(order_id) is not int:
            raise TypeError("order_id must be int")
        if type(customer_id) is not int:
            raise TypeError("customer_id must be int")
        if not isinstance(amount, Decimal):
            raise TypeError("amount must be decimal")
        if not isinstance(status, str):
            raise TypeError("status must be text")
        if status.strip() == "":
            raise ValueError("status cant be empty")
        self.order_id = order_id
        self.customer_id = customer_id
        self.amount = amount
        self.status = status.strip().lower()

    def is_paid(self) -> bool:
        return self.status == "paid"

    def is_cancelled(self) -> bool:
        return self.status == "cancelled"
