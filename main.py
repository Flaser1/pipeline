

from config import load_config
from pipeline import run_pipeline
from transformations import normalize_customers, normalize_orders
from metrics import build_summary_country, build_summary_status
from reporting import print_countries_report, print_statuses_report, print_invalid

def main():
    config_customers, expected_columns_customers = load_config("CUSTOMERS")
    config_orders, expected_columns_orders = load_config("ORDERS")

    customers_raw_csv = run_pipeline(config_customers.input_path, config_customers.output_dir, expected_columns_customers)
    orders_raw_csv = run_pipeline(config_orders.input_path, config_orders.output_dir, expected_columns_orders)

    clean_customers, invalid_customers = normalize_customers(customers_raw_csv)
    clean_orders, invalid_orders = normalize_orders(orders_raw_csv)

    countries_summary = build_summary_country(clean_customers, clean_orders)
    statuses_summary = build_summary_status(clean_customers, clean_orders)

    print_countries_report(countries_summary)
    print_statuses_report(statuses_summary)
    print_invalid(invalid_orders)
    print_invalid(invalid_customers)

if __name__ == "__main__":
    main()