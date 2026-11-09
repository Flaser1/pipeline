

from models import Customer, Order

def build_summary_country(customers: list[Customer], orders: list[Order]) -> dict:
    countries_summary = {}
    paying_customers = {}
    for customer in customers:
        country = customer.country
        if country not in countries_summary:
            countries_summary[country] = {
                "customers_count": 0,
                "paying_customers_count": 0,
                "orders_count": 0,
                "paid_orders_count": 0,
                "cancelled_orders_count": 0,
                "total_revenue": 0,
                "paid_revenue": 0,
                "cancelled_revenue": 0,
            }
            paying_customers[country] = set()
        countries_summary[country]["customers_count"] += 1

    customers_country = {customer.customer_id: customer.country for customer in customers}
    for order in orders:
        customer_id = order.customer_id
        country = customers_country.get(customer_id)
        if country is None:
            continue
        countries_summary[country]["total_revenue"] += order.amount
        countries_summary[country]["orders_count"] += 1
        if order.is_paid() == True:
            countries_summary[country]["paid_orders_count"] += 1
            countries_summary[country]["paid_revenue"] += order.amount
            paying_customers[country].add(customer_id)
        if order.is_cancelled() == True:
            countries_summary[country]["cancelled_revenue"] += order.amount
            countries_summary[country]["cancelled_orders_count"] += 1

    for country in countries_summary:
        countries_summary[country]["paying_customers_count"] = len(paying_customers[country])

    return countries_summary

def build_summary_status(customers: list[Customer], orders: list[Order]) -> dict:
    status_summaries = {}
    status_customers = {}
    customers_ids = {customer.customer_id for customer in customers}
    for order in orders:
        status = order.status
        if order.customer_id not in customers_ids:
            continue
        if status not in status_summaries:
            status_summaries[status] = {
                "customers_count": 0,
                "orders_count": 0,
                "revenue": 0,
            }
            status_customers[status] = set()
        status_summaries[status]["orders_count"] += 1
        status_summaries[status]["revenue"] += order.amount
        status_customers[status].add(order.customer_id)

    for status in status_customers:
        status_summaries[status]["customers_count"] = len(status_customers[status])

    return status_summaries







